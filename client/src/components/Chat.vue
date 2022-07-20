<template>
<input
      type="text"
        outline
        animate-bounce-in
        rounded
        mx-16
        my-4
        text-gray-500
        text-sm
        p-1
        h-8
        br
        
        @keyup.enter="sendMessage"
        @keyup.esc="close"
        @keyup.backspace="clear"
        :v-model="message"
        placeholder='Send a message'
        />
  <p>{{message}}</p>
</template>
<script setup lang="ts">
const props = defineProps({
    user: {
        type: Object,
        required: true
    }
})

var message = ref('');

const clear = () => {
    message.value = '';
}

</script>