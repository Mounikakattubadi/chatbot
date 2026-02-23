<template>
  <div class="w-full flex" :class="isUser ? 'justify-end' : 'justify-start'">
    <div
      :class="bubbleClass"
      class="px-4 py-3 max-w-[70%] rounded-2xl shadow-lg text-sm leading-relaxed animate-fadeIn"
    >
      {{ message }}
    </div>
  </div>
</template>

<script>
export default {
  props: ["message", "isUser"],
  computed: {
    bubbleClass() {
      return this.isUser
        ? "bg-blue-600 text-white rounded-br-none"
        : "bg-[#1a1a1a] text-gray-200 border border-gray-700 rounded-bl-none";
    }
  }
};
</script>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fadeIn {
  animation: fadeIn 0.2s ease-out;
}
</style>
