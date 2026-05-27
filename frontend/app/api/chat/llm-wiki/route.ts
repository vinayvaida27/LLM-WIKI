export const runtime = "nodejs"

const DEFAULT_BACKEND_URL = "http://127.0.0.1:8000"

export async function POST(request: Request) {
  const body = await request.json()
  const backendUrl =
    process.env.LLM_WIKI_API_BASE_URL ||
    process.env.NEXT_PUBLIC_LLM_WIKI_API_BASE_URL ||
    DEFAULT_BACKEND_URL

  const response = await fetch(`${backendUrl}/v1/chat/completions`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: body.model || "llm-wiki",
      messages: body.messages,
      temperature: body.temperature ?? 0.2,
      top_k: body.top_k ?? 6,
      stream: body.stream ?? true,
      enable_hyde: body.enable_hyde ?? false,
      enable_query_expansion: body.enable_query_expansion ?? false
    })
  })

  if (!response.ok) {
    const errorText = await response.text()

    return new Response(
      JSON.stringify({
        message: errorText || "LLM Wiki backend request failed"
      }),
      {
        status: response.status,
        headers: {
          "Content-Type": "application/json"
        }
      }
    )
  }

  return new Response(response.body, {
    status: response.status,
    headers: {
      "Content-Type": response.headers.get("Content-Type") || "text/event-stream"
    }
  })
}
