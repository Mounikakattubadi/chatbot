<template>
  <div class="flex mt-4">
    <input
      v-model="userMessage"
      @keyup.enter="sendMessage"
      placeholder="Type your message..."
      class="flex-1 p-2 border rounded-l-lg focus:outline-none"
    />
    <button
      @click="sendMessage"
      class="bg-blue-500 text-white px-4 rounded-r-lg"
    >
      Send
    </button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  emits: ["send"],

  setup(_, { emit }) {
    const userMessage = ref<string>("");

    const sendMessage = () => {
      if (userMessage.value.trim() !== "") {
        emit("send", userMessage.value);
        userMessage.value = "";
      }
    };

    return { userMessage, sendMessage };
  }
});
</script>
