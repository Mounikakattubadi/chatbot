<template>
  <div class="p-4 bg-[#111] border-t border-gray-800 flex gap-3">
    <input
      v-model="text"
      @keyup.enter="sendMsg"
      type="text"
      placeholder="Type your message…"
      class="flex-1 p-3 bg-[#1a1a1a] border border-gray-700 rounded-xl text-gray-200 focus:ring-2 focus:ring-blue-500 outline-none"
    />

    <button
      @click="sendMsg"
      class="px-6 py-3 bg-blue-600 rounded-xl text-white font-medium hover:bg-blue-700"
    >
      Send
    </button>
  </div>
</template>

<script>
export default {
  emits: ["send"],
  data() {
    return { text: "" };
  },
  methods: {
    sendMsg() {
      if (!this.text.trim()) return;
      this.$emit("send", this.text);
      this.text = "";
    }
  }
};
</script>
