"use client"

import { MessageMarkdown } from "@/components/messages/message-markdown"
import { Button } from "@/components/ui/button"
import { TextareaAutosize } from "@/components/ui/textarea-autosize"
import { IconPlayerStop, IconSend, IconSparkles } from "@tabler/icons-react"
import { useRef, useState } from "react"

type ChatMessage = {
  role: "user" | "assistant"
  content: string
}

const starterMessages: ChatMessage[] = [
  {
    role: "assistant",
    content:
      "Ask me about the LLM Wiki. I will route your question to the FastAPI RAG backend and answer from the indexed wiki context."
  }
]

function readSSEContent(buffer: string) {
  let content = ""
  const events = buffer.split("\n\n")

  for (const event of events) {
    const dataLine = event
      .split("\n")
      .find(line => line.startsWith("data: "))

    if (!dataLine) continue

    const data = dataLine.slice(6).trim()
    if (!data || data === "[DONE]") continue

    try {
      const parsed = JSON.parse(data)
      content += parsed.choices?.[0]?.delta?.content || ""
    } catch {
      continue
    }
  }

  return content
}

function MessageContent({ message }: { message: ChatMessage }) {
  if (!message.content) {
    return <div className="text-sm leading-6">Thinking...</div>
  }

  if (message.role === "user") {
    return (
      <div className="whitespace-pre-wrap text-sm leading-6">
        {message.content}
      </div>
    )
  }

  return (
    <div className="overflow-x-auto text-sm leading-6">
      <MessageMarkdown content={message.content} />
    </div>
  )
}

export default function LLMWikiPage() {
  const [messages, setMessages] = useState<ChatMessage[]>(starterMessages)
  const [input, setInput] = useState("")
  const [topK, setTopK] = useState(6)
  const [isGenerating, setIsGenerating] = useState(false)
  const abortRef = useRef<AbortController | null>(null)

  const sendMessage = async () => {
    const trimmed = input.trim()
    if (!trimmed || isGenerating) return

    const nextMessages: ChatMessage[] = [
      ...messages,
      { role: "user", content: trimmed },
      { role: "assistant", content: "" }
    ]

    setMessages(nextMessages)
    setInput("")
    setIsGenerating(true)
    requestAnimationFrame(() => {
      window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" })
    })

    const controller = new AbortController()
    abortRef.current = controller

    try {
      const response = await fetch("/api/chat/llm-wiki", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        signal: controller.signal,
        body: JSON.stringify({
          messages: nextMessages
            .filter(message => message.content)
            .map(message => ({
              role: message.role,
              content: message.content
            })),
          top_k: topK,
          stream: true
        })
      })

      if (!response.ok || !response.body) {
        const error = await response.json().catch(() => ({
          message: "The LLM Wiki backend did not return a stream."
        }))
        throw new Error(error.message)
      }

      const reader = response.body.getReader()
      const decoder = new TextDecoder()
      let assistantText = ""
      let sseBuffer = ""

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        sseBuffer += decoder.decode(value, { stream: true })
        const events = sseBuffer.split("\n\n")
        sseBuffer = events.pop() || ""

        assistantText += readSSEContent(events.join("\n\n"))

        setMessages(current =>
          current.map((message, index) =>
            index === current.length - 1
              ? { ...message, content: assistantText }
              : message
          )
        )
      }

      sseBuffer += decoder.decode()
      if (sseBuffer.trim()) {
        assistantText += readSSEContent(sseBuffer)

        setMessages(current =>
          current.map((message, index) =>
            index === current.length - 1
              ? { ...message, content: assistantText }
              : message
          )
        )
      }
    } catch (error: any) {
      if (error.name !== "AbortError") {
        setMessages(current =>
          current.map((message, index) =>
            index === current.length - 1
              ? {
                  ...message,
                  content:
                    error.message ||
                    "Could not reach the LLM Wiki backend. Check that FastAPI is running on port 8000."
                }
              : message
          )
        )
      }
    } finally {
      setIsGenerating(false)
      abortRef.current = null
    }
  }

  const stopMessage = () => {
    abortRef.current?.abort()
    setIsGenerating(false)
  }

  return (
    <main className="min-h-screen w-full">
      <header className="sticky top-0 z-20 border-b bg-background/95 px-4 py-3 backdrop-blur">
        <div className="mx-auto flex w-full max-w-5xl items-center justify-between gap-3">
          <div className="flex min-w-0 items-center gap-3">
            <IconSparkles className="shrink-0" size={24} />
            <div className="min-w-0">
              <h1 className="truncate text-lg font-semibold">LLM Wiki Chat</h1>
              <p className="text-muted-foreground truncate text-sm">
                Connected to FastAPI at /v1/chat/completions
              </p>
            </div>
          </div>

          <label className="flex items-center gap-2 text-sm">
            <span className="text-muted-foreground">Top K</span>
            <input
              className="bg-background border-input h-9 w-16 rounded-md border px-2"
              max={20}
              min={1}
              type="number"
              value={topK}
              onChange={event => setTopK(Number(event.target.value))}
            />
          </label>
        </div>
      </header>

      <section className="mx-auto flex w-full max-w-5xl flex-col gap-4 px-4 py-5 pb-32">
        {messages.map((message, index) => (
          <article
            className={
              message.role === "user"
                ? "ml-auto max-w-[85%] rounded-md bg-primary px-4 py-3 text-primary-foreground"
                : "mr-auto max-w-[92%] overflow-hidden rounded-md border bg-muted/30 px-4 py-3"
            }
            key={`${message.role}-${index}`}
          >
            <MessageContent message={message} />
          </article>
        ))}
      </section>

      <footer className="sticky bottom-0 z-20 border-t bg-background/95 p-4 backdrop-blur">
        <div className="mx-auto flex w-full max-w-5xl items-end gap-2">
          <TextareaAutosize
            className="min-h-[52px] flex-1 resize-none rounded-md border px-3 py-2"
            maxRows={6}
            onKeyDown={event => {
              if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault()
                sendMessage()
              }
            }}
            onValueChange={setInput}
            placeholder="Ask about HMMs, sequence alignment, protein language models..."
            value={input}
          />

          {isGenerating ? (
            <Button
              aria-label="Stop generation"
              onClick={stopMessage}
              size="icon"
              type="button"
              variant="secondary"
            >
              <IconPlayerStop size={20} />
            </Button>
          ) : (
            <Button
              aria-label="Send message"
              disabled={!input.trim()}
              onClick={sendMessage}
              size="icon"
              type="button"
            >
              <IconSend size={20} />
            </Button>
          )}
        </div>
      </footer>
    </main>
  )
}
