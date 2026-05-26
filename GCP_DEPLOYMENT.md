# GCP Deployment Guide For LLM-WIKI

This guide deploys the LLM-WIKI project to Google Cloud using only the browser and Cloud Shell.

It includes the fixes needed during the first deployment:

- Cloud Build storage permissions.
- Artifact Registry push permissions.
- Cloud Run secret access permissions.
- Cloud Logging writer permissions.
- Docker BuildKit for the backend build.
- Frontend runtime dependency fix for `@next/bundle-analyzer`.
- OpenAI secret formatting without a trailing newline.
- Commands to monitor user questions.

Do not paste real API keys into GitHub, README files, screenshots, chat logs, or commit history.

## Final Architecture

```text
User Browser
  -> Cloud Run frontend: Next.js Chat UI
  -> POST /api/chat/llm-wiki
  -> Cloud Run backend: FastAPI RAG API
  -> searches llm-wiki retrieval files
  -> calls OpenAI through LiteLLM
  -> streams the answer back to the browser
```

## 1. Open Google Cloud Shell

1. Go to https://console.cloud.google.com
2. Select your GCP project.
3. Click the Cloud Shell icon in the top-right.

Clone the repo:

```bash
git clone https://github.com/vinayvaida27/LLM-WIKI.git
cd LLM-WIKI
```

Check the files:

```bash
ls
```

You should see:

```text
backend  frontend  llm-wiki  README.md
```

Optional browser editor:

```bash
cloudshell edit .
```

## 2. Set Variables

Run these in Cloud Shell:

```bash
export PROJECT_ID=$(gcloud config get-value project)
export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
export REGION=us-central1
export REPO=llm-wiki
export BACKEND_IMAGE="$REGION-docker.pkg.dev/$PROJECT_ID/$REPO/llm-wiki-api:latest"
```

## 3. Enable GCP Services

```bash
gcloud services enable \
  run.googleapis.com \
  cloudbuild.googleapis.com \
  artifactregistry.googleapis.com \
  secretmanager.googleapis.com \
  logging.googleapis.com
```

## 4. Grant Required Permissions

These permissions fixed the deployment errors we hit.

Cloud Build source upload/read access:

```bash
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
```

Cloud Build service account storage access:

```bash
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
```

Artifact Registry write access:

```bash
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
  --role="roles/artifactregistry.writer"
```

Cloud Logging write access:

```bash
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
  --role="roles/logging.logWriter"
```

Secret Manager access for Cloud Run:

```bash
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

## 5. Create Artifact Registry Repository

Run once:

```bash
gcloud artifacts repositories create $REPO \
  --repository-format=docker \
  --location=$REGION \
  --description="LLM-WIKI containers"
```

If it says the repository already exists, continue.

## 6. Add OpenAI API Key Secret

Use `printf`, not `echo`, so the secret does not include a trailing newline.

```bash
printf '%s' 'PASTE_YOUR_OPENAI_API_KEY_HERE' | \
  gcloud secrets create OPENAI_API_KEY --data-file=-
```

If the secret already exists, add a new version:

```bash
printf '%s' 'PASTE_YOUR_OPENAI_API_KEY_HERE' | \
  gcloud secrets versions add OPENAI_API_KEY --data-file=-
```

Check that the secret does not end with a newline without printing the key:

```bash
gcloud secrets versions access latest --secret=OPENAI_API_KEY | \
  python3 -c "import sys; s=sys.stdin.buffer.read(); print('ends_newline=', s.endswith(b'\n'), 'length=', len(s))"
```

Expected:

```text
ends_newline= False
```

Important: if an API key was ever pasted into logs, screenshots, or chat, rotate/delete that key in the OpenAI dashboard and use a new one.

## 7. Build Backend Image

Run from the repo root:

```bash
cd ~/LLM-WIKI

gcloud builds submit \
  --config cloudbuild.backend.yaml \
  --substitutions _IMAGE=$BACKEND_IMAGE \
  .
```

Fix included in this repo:

```yaml
env:
  - DOCKER_BUILDKIT=1
```

This is needed because the backend Dockerfile uses:

```dockerfile
RUN --mount=type=cache,target=/root/.cache/uv ...
```

Without BuildKit, Cloud Build fails with:

```text
the --mount option requires BuildKit
```

## 8. Deploy Backend

```bash
gcloud run deploy llm-wiki-api \
  --image $BACKEND_IMAGE \
  --region $REGION \
  --allow-unauthenticated \
  --memory 1Gi \
  --cpu 1 \
  --set-env-vars MODEL_NAME=gpt-4.1-mini,LLM_WIKI_ROOT=/app \
  --set-secrets OPENAI_API_KEY=OPENAI_API_KEY:latest
```

Save backend URL:

```bash
export BACKEND_URL=$(gcloud run services describe llm-wiki-api \
  --region $REGION \
  --format='value(status.url)')

echo $BACKEND_URL
```

Test backend:

```bash
curl "$BACKEND_URL/health"
```

Success looks like:

```json
{"status":"ok"}
```

## 9. Deploy Frontend

```bash
cd ~/LLM-WIKI/frontend

gcloud run deploy llm-wiki-frontend \
  --source . \
  --region $REGION \
  --allow-unauthenticated \
  --memory 1Gi \
  --set-env-vars LLM_WIKI_API_BASE_URL=$BACKEND_URL,NEXT_PUBLIC_LLM_WIKI_API_BASE_URL=$BACKEND_URL
```

Open the frontend URL printed by Cloud Run.

The LLM Wiki page is:

```text
https://YOUR_FRONTEND_URL/llm-wiki
```

or:

```text
https://YOUR_FRONTEND_URL/en/llm-wiki
```

## 10. Fixes Already Added To The Repo

### Backend includes wiki files

The backend Dockerfile copies the wiki and retrieval files into the backend image:

```dockerfile
COPY llm-wiki/retrieval /app/retrieval
COPY llm-wiki/Wiki      /app/Wiki
COPY llm-wiki/Raw       /app/Raw
COPY llm-wiki/Schema    /app/Schema
```

This is why `LLM_WIKI_ROOT=/app` works in Cloud Run.

### Backend strips newline from secrets

The backend now strips whitespace from provider API keys before LiteLLM uses them.

This prevents:

```text
Illegal header value b'Bearer ...\n'
```

### Frontend runtime dependency fixed

Cloud Run failed with:

```text
Cannot find module '@next/bundle-analyzer'
```

Fix: `@next/bundle-analyzer` was moved from `devDependencies` to production `dependencies`.

### Backend logs user questions

The backend logs each chat request as structured JSON:

```json
{
  "event": "chat_request",
  "endpoint": "/v1/chat/completions",
  "question": "What is HMM?",
  "top_k": 6,
  "source_count": 6,
  "sources": []
}
```

## 11. Monitor User Questions

Read recent backend logs:

```bash
gcloud run services logs read llm-wiki-api \
  --region us-central1 \
  --limit 100
```

Show only chat requests:

```bash
gcloud run services logs read llm-wiki-api \
  --region us-central1 \
  --limit 100 | grep chat_request
```

Tail live logs. Some Cloud Shell versions require `beta`:

```bash
gcloud beta run services logs tail llm-wiki-api \
  --region us-central1
```

In the browser:

```text
Google Cloud Console -> Cloud Run -> llm-wiki-api -> Logs
```

## 12. Common Errors And Fixes

### `fatal: not a git repository`

You are not inside the repo.

```bash
cd ~/LLM-WIKI
git pull
```

### `storage.objects.get access denied`

Grant storage viewer:

```bash
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
```

### `artifactregistry.repositories.uploadArtifacts denied`

Grant Artifact Registry writer:

```bash
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
  --role="roles/artifactregistry.writer"
```

### `Permission denied on secret OPENAI_API_KEY`

Grant Secret Manager accessor:

```bash
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

### Frontend says `Service Unavailable`

Check logs:

```bash
gcloud run services logs read llm-wiki-frontend \
  --region us-central1 \
  --limit 80
```

If logs say `Cannot find module '@next/bundle-analyzer'`, pull latest repo and redeploy frontend:

```bash
cd ~/LLM-WIKI
git pull

cd frontend
gcloud run deploy llm-wiki-frontend \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 1Gi \
  --set-env-vars LLM_WIKI_API_BASE_URL=$BACKEND_URL,NEXT_PUBLIC_LLM_WIKI_API_BASE_URL=$BACKEND_URL
```

### Chat returns `OpenAIException - Connection error`

Check backend logs:

```bash
gcloud run services logs read llm-wiki-api \
  --region us-central1 \
  --limit 100
```

If logs mention `Illegal header value` or show `Bearer ...\n`, the OpenAI key secret has a trailing newline.

Fix by adding a new secret version with `printf`:

```bash
printf '%s' 'PASTE_YOUR_NEW_OPENAI_API_KEY_HERE' | \
  gcloud secrets versions add OPENAI_API_KEY --data-file=-
```

Then rebuild and redeploy the backend.

## 13. Update Existing Deployment Later

Pull latest code:

```bash
cd ~/LLM-WIKI
git pull
```

Rebuild backend only when backend code or wiki files changed:

```bash
gcloud builds submit \
  --config cloudbuild.backend.yaml \
  --substitutions _IMAGE=$BACKEND_IMAGE \
  .

gcloud run deploy llm-wiki-api \
  --image $BACKEND_IMAGE \
  --region $REGION \
  --allow-unauthenticated \
  --memory 1Gi \
  --cpu 1 \
  --set-env-vars MODEL_NAME=gpt-4.1-mini,LLM_WIKI_ROOT=/app \
  --set-secrets OPENAI_API_KEY=OPENAI_API_KEY:latest
```

Redeploy frontend only when frontend code changed:

```bash
cd ~/LLM-WIKI/frontend

gcloud run deploy llm-wiki-frontend \
  --source . \
  --region $REGION \
  --allow-unauthenticated \
  --memory 1Gi \
  --set-env-vars LLM_WIKI_API_BASE_URL=$BACKEND_URL,NEXT_PUBLIC_LLM_WIKI_API_BASE_URL=$BACKEND_URL
```

