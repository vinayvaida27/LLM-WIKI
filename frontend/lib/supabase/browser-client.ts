import { Database } from "@/supabase/types"
import { createBrowserClient } from "@supabase/ssr"
import { SupabaseClient } from "@supabase/supabase-js"

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY

function missingSupabaseClient() {
  throw new Error(
    "Supabase is not configured. Set NEXT_PUBLIC_SUPABASE_URL and NEXT_PUBLIC_SUPABASE_ANON_KEY to use the full Chatbot UI app. The LLM Wiki chat page does not require Supabase."
  )
}

export const supabase =
  supabaseUrl && supabaseAnonKey
    ? createBrowserClient<Database>(supabaseUrl, supabaseAnonKey)
    : new Proxy({} as SupabaseClient<Database>, {
        get(_target, property) {
          if (property === "then") return undefined
          return missingSupabaseClient()
        }
      })
