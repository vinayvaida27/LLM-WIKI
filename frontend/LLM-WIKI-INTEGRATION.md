# LLM Wiki Frontend Integration

This folder is a clone of `mckaywrigley/chatbot-ui` with an added no-auth LLM Wiki chat page.

## Backend

From the repo root:

```powershell
cd D:\pythonProject\GEN-AI\Build-LLM-WIKI\backend
$env:LLM_WIKI_ROOT="D:\pythonProject\GEN-AI\Build-LLM-WIKI\llm-wiki"
uv run python app.py
```

Verify:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

## Frontend

From this folder:

```powershell
cd "D:\pythonProject\GEN-AI\Build-LLM-WIKI\frontend"
npm.cmd install
npm.cmd run dev -- -p 3000
```

Open:

```text
http://localhost:3000/en/llm-wiki
```

## Integration Points

- `app/api/chat/llm-wiki/route.ts` proxies frontend requests to the FastAPI backend.
- `app/[locale]/llm-wiki/page.tsx` is the simple no-auth chat page.
- `.env.local` controls the backend URL:

```env
LLM_WIKI_API_BASE_URL=http://127.0.0.1:8000
NEXT_PUBLIC_LLM_WIKI_API_BASE_URL=http://127.0.0.1:8000
```

The full stock Chatbot UI workflow still exists, but it requires Supabase setup.
