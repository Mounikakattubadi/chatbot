<template>
  <div :class="isUser ? 'justify-end' : 'justify-start'" class="flex mb-2">
    <div
      :class="isUser ? 'bg-blue-500 text-white' : 'bg-gray-200 text-gray-800'"
      class="p-3 rounded-lg max-w-xs break-words"
    >
      {{ message }}
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    message: { type: String, required: true },
    isUser: { type: Boolean, required: true }
  }
});
</script>
