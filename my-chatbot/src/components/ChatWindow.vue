<template>
  <div
    id="chatWindow"
    class="flex-1 overflow-y-auto px-6 py-6 bg-[#0f0f0f] space-y-4"
  >
    <MessageBubble
      v-for="(msg, i) in messages"
      :key="i"
      :message="msg.text"
      :isUser="msg.user"
    />
  </div>
</template>

<script>
import { onMounted, onUpdated } from "vue";
import MessageBubble from "./MessageBubble.vue";

export default {
  props: ["messages"],
  components: { MessageBubble },
  setup() {

    // ⬇️ CALL YOUR BACKEND HERE
    onMounted(async () => {
      const api = import.meta.env.VITE_API_URL;

      try {
        const res = await fetch(`${api}/hello`);
        const data = await res.json();

        console.log("Backend Response:", data);
      } catch (err) {
        console.error("Backend API Error:", err);
      }
    });

    // auto-scroll when messages update
    onUpdated(() => {
      const el = document.getElementById("chatWindow");
      el?.scrollTo({ top: el.scrollHeight, behavior: "smooth" });
    });
  }
};
</script>

<style scoped>
::-webkit-scrollbar {
  width: 6px;
}
::-webkit-scrollbar-track {
  background: #111;
}
::-webkit-scrollbar-thumb {
  background: #2e2e2e;
  border-radius: 10px;
}
</style>