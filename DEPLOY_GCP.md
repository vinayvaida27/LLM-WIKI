# Deploy LLM-WIKI To Google Cloud Run

This guide assumes you already:

1. Opened Google Cloud Shell.
2. Cloned this repo.
3. Enabled Cloud Run, Cloud Build, Artifact Registry, Secret Manager, and Logging.
4. Created the `OPENAI_API_KEY` secret.

## 1. Set Variables

```bash
export PROJECT_ID=$(gcloud config get-value project)
export REGION=us-central1
export REPO=llm-wiki
export BACKEND_IMAGE="$REGION-docker.pkg.dev/$PROJECT_ID/$REPO/llm-wiki-api:latest"
```

## 2. Create Artifact Registry Repo

Run this once:

```bash
gcloud artifacts repositories create $REPO \
  --repository-format=docker \
  --location=$REGION \
  --description="LLM-WIKI containers"
```

If it says the repo already exists, that is fine.

## Secret Format

When creating or updating `OPENAI_API_KEY`, use `printf` so the secret does not contain a trailing newline:

```bash
printf '%s' 'YOUR_OPENAI_API_KEY' | gcloud secrets versions add OPENAI_API_KEY --data-file=-
```

## 3. Build Backend Image

Run from the repo root:

```bash
gcloud builds submit \
  --config cloudbuild.backend.yaml \
  --substitutions _IMAGE=$BACKEND_IMAGE \
  .
```

## 4. Deploy Backend

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

Save the backend URL:

```bash
export BACKEND_URL=$(gcloud run services describe llm-wiki-api \
  --region $REGION \
  --format='value(status.url)')

echo $BACKEND_URL
```

Test it:

```bash
curl "$BACKEND_URL/health"
```

## 5. Deploy Frontend

```bash
cd frontend

gcloud run deploy llm-wiki-frontend \
  --source . \
  --region $REGION \
  --allow-unauthenticated \
  --memory 1Gi \
  --set-env-vars LLM_WIKI_API_BASE_URL=$BACKEND_URL,NEXT_PUBLIC_LLM_WIKI_API_BASE_URL=$BACKEND_URL
```

Open the frontend URL printed by Cloud Run.

## 6. Monitor User Inputs

The backend logs each chat request as a structured JSON line with:

- `event`
- `endpoint`
- `question`
- `top_k`
- `source_count`
- top retrieved source paths

View logs:

```bash
gcloud run services logs read llm-wiki-api \
  --region $REGION \
  --limit 50
```

Follow live logs:

```bash
gcloud run services logs tail llm-wiki-api \
  --region $REGION
```

In the browser:

```text
Google Cloud Console -> Cloud Run -> llm-wiki-api -> Logs
```

Do not log passwords, API keys, or private user information.
