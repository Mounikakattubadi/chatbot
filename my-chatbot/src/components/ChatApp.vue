<template>
  <div class="p-6 max-w-lg mx-auto">
    <!-- Chat display -->
    <ChatWindow :messages="messages" />

    <!-- Input box for user -->
    <InputBox @send="handleUserMessage" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import ChatWindow from './ChatWindow.vue'
import InputBox from './InputBox.vue'

type Message = { text: string; user: boolean }

const messages = ref<Message[]>([])

async function sendToBackend(message: string) {
  try {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    })

    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`)
    }

    const data = await res.json()
    return data.reply
  } catch (error) {
    console.error("Error sending message to backend:", error)
    return "Sorry, I'm not available right now."
  }
}

async function handleUserMessage(msg: string) {
  // Add user's message to chat
  messages.value.push({ text: msg, user: true })

  // Get bot reply
  const reply = await sendToBackend(msg)

  // Add bot reply to chat
  messages.value.push({ text: reply, user: false })
}
</script>
