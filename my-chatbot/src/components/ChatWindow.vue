<template>
  <div
    class="flex flex-col h-[80vh] p-4 border rounded-lg bg-gray-50 overflow-y-auto"
  >
    <MessageBubble
      v-for="(msg, index) in messages"
      :key="index"
      :message="msg.text"
      :isUser="msg.user"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import MessageBubble from "./MessageBubble.vue";

interface ChatMessage {
  text: string;
  user: boolean;
}

export default defineComponent({
  components: { MessageBubble },

  props: {
    messages: {
      type: Array as PropType<ChatMessage[]>,
      required: true
    }
  }
});
</script>
