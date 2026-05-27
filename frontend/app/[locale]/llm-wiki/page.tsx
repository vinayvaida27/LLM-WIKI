"use client"

import { MessageMarkdown } from "@/components/messages/message-markdown"
import { Button } from "@/components/ui/button"
import { TextareaAutosize } from "@/components/ui/textarea-autosize"
import {
  IconChevronDown,
  IconPlayerStop,
  IconSend,
  IconSparkles
} from "@tabler/icons-react"
import { useEffect, useRef, useState } from "react"

// ── Model definitions ────────────────────────────────────────────────────────

const MODELS = [
  {
    id: "gpt-4.1-mini",
    label: "Quick",
    sublabel: "gpt-4.1-mini",
    description: "Fast answers, low latency"
  },
  {
    id: "gpt-4.1",
    label: "Standard",
    sublabel: "gpt-4.1",
    description: "Better coding & long context"
  },
  {
    id: "o3",
    label: "Reasoning",
    sublabel: "o3",
    description: "Deep multi-step reasoning"
  }
] as const

type ModelId = (typeof MODELS)[number]["id"]

/** Dropdown to switch between the three backend models. */
function ModelPicker({
  value,
  onChange
}: {
  value: ModelId
  onChange: (id: ModelId) => void
}) {
  const [open, setOpen] = useState(false)
  const ref = useRef<HTMLDivElement>(null)
  const current = MODELS.find(m => m.id === value)!

  // Close when clicking outside
  useEffect(() => {
    if (!open) return
    function handleOutside(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setOpen(false)
      }
    }
    document.addEventListener("mousedown", handleOutside)
    return () => document.removeEventListener("mousedown", handleOutside)
  }, [open])

  return (
    <div ref={ref} className="relative">
      {/* Trigger button — matches the "Extended ∨" style */}
      <button
        type="button"
        onClick={() => setOpen(v => !v)}
        className={[
          "flex items-center gap-1.5 rounded-md border px-3 py-1.5 text-sm font-medium",
          "transition-colors duration-150 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
          open
            ? "border-primary bg-accent text-foreground"
            : "border-input bg-background text-foreground hover:bg-accent hover:text-accent-foreground"
        ].join(" ")}
      >
        {current.label}
        <IconChevronDown
          size={14}
          className={`transition-transform duration-200 ${open ? "rotate-180" : ""}`}
        />
      </button>

      {/* Dropdown panel */}
      {open && (
        <div className="absolute right-0 top-full z-50 mt-1.5 min-w-[210px] overflow-hidden rounded-lg border bg-popover shadow-lg">
          {MODELS.map(m => {
            const active = m.id === value
            return (
              <button
                key={m.id}
                type="button"
                onClick={() => {
                  onChange(m.id)
                  setOpen(false)
                }}
                className={[
                  "flex w-full items-start gap-2.5 px-3 py-2.5 text-left transition-colors hover:bg-accent",
                  active ? "bg-accent/50" : ""
                ].join(" ")}
              >
                {/* Active dot */}
                <span className="mt-1.5 flex size-4 shrink-0 items-center justify-center">
                  {active && (
                    <span className="size-2 rounded-full bg-primary" />
                  )}
                </span>

                <span className="flex flex-col gap-0.5">
                  <span className="flex items-baseline gap-1.5">
                    <span className="text-sm font-medium">{m.label}</span>
                    <span className="text-muted-foreground text-[11px]">
                      {m.sublabel}
                    </span>
                  </span>
                  <span className="text-muted-foreground text-xs">
                    {m.description}
                  </span>
                </span>
              </button>
            )
          })}
        </div>
      )}
    </div>
  )
}

/** Pill-shaped toggle used for HyDE and Query Expansion controls. */
function ToggleChip({
  label,
  active,
  onClick,
  tooltip
}: {
  label: string
  active: boolean
  onClick: () => void
  tooltip: string
}) {
  return (
    <button
      title={tooltip}
      type="button"
      onClick={onClick}
      className={[
        "inline-flex items-center gap-1.5 rounded-full border px-3 py-1 text-xs font-medium",
        "transition-colors duration-150 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring",
        active
          ? "border-primary bg-primary text-primary-foreground"
          : "border-input bg-background text-muted-foreground hover:border-primary/60 hover:text-foreground"
      ].join(" ")}
    >
      <span
        className={[
          "size-1.5 rounded-full",
          active ? "bg-primary-foreground" : "bg-muted-foreground"
        ].join(" ")}
      />
      {label}
    </button>
  )
}

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
  const [model, setModel] = useState<ModelId>("gpt-4.1-mini")
  const [topK, setTopK] = useState(6)
  const [enableHyde, setEnableHyde] = useState(false)
  const [enableExpansion, setEnableExpansion] = useState(false)
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
          model,
          messages: nextMessages
            .filter(message => message.content)
            .map(message => ({
              role: message.role,
              content: message.content
            })),
          top_k: topK,
          stream: true,
          enable_hyde: enableHyde,
          enable_query_expansion: enableExpansion
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

          <div className="flex items-center gap-3">
            <ModelPicker value={model} onChange={setModel} />

            <div className="bg-border h-5 w-px" />

            <ToggleChip
              active={enableHyde}
              label="HyDE"
              tooltip="Hypothetical Document Embeddings — generate a draft answer and use it as the retrieval query for deeper semantic matching"
              onClick={() => setEnableHyde(v => !v)}
            />
            <ToggleChip
              active={enableExpansion}
              label="Expand"
              tooltip="Query Expansion — generate 2 alternative phrasings and merge BM25 results from all variants for broader recall"
              onClick={() => setEnableExpansion(v => !v)}
            />

            <div className="bg-border h-5 w-px" />

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
