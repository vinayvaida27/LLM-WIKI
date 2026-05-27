export const runtime = "nodejs"

const DEFAULT_BACKEND_URL = "http://127.0.0.1:8000"

interface RouteContext {
  params: {
    sourceId: string
  }
}

export async function GET(_request: Request, { params }: RouteContext) {
  const backendUrl =
    process.env.LLM_WIKI_API_BASE_URL ||
    process.env.NEXT_PUBLIC_LLM_WIKI_API_BASE_URL ||
    DEFAULT_BACKEND_URL

  const response = await fetch(
    `${backendUrl}/sources/${encodeURIComponent(params.sourceId)}`,
    {
      method: "GET",
      headers: {
        Accept: "text/html"
      }
    }
  )

  if (!response.ok) {
    const errorText = await response.text()

    return new Response(errorText || "Citation source not found", {
      status: response.status,
      headers: {
        "Content-Type": "text/plain; charset=utf-8"
      }
    })
  }

  return new Response(await response.text(), {
    status: response.status,
    headers: {
      "Content-Type":
        response.headers.get("Content-Type") || "text/html; charset=utf-8"
    }
  })
}
