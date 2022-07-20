<style scoped>
.submit {
  @apply bg-blue-500 hover:bg-lime-300 hover:text-blue-900 hover:border-2 hover:border-blue-900 hover:shadow-lg @apply animate_animated hover:shadow-gray-500 text-white font-bold py-2 px-4 rounded cursor-pointer;
}
</style>
<template>
  <form @submit.prevent="onSubmit" col center bg-teal-500 rounded-xl shadow>
    <div backdrop-filter-blur-20   bg-transparent  >
      <div col m-4>
        <label for="from" mx-8 p-8 text-md  text="center" font-mono>Email</label>
        <input
          type="email"
          id="from"
          v-model="from"
          placeholder="Your email, example: john.doe@example.com"
          input
         bg-blue-800 hover:bg-lime-300  hover:border-2 hover:text-gray-700 hover:border-blue-900 hover:shadow-lg hover:shadow-gray-500 text-white font-bold py-2 px-4 rounded
        />
        <label for="name" mx-4 mt-4 p="x4 y2" text="center" font-mono>Name</label>
        <input
          type="text"
          id="name"
          v-model="name"
          placeholder="Your name, example: John Doe"
          input
          bg-blue-800 hover:bg-lime-300  hover:border-2 hover:text-gray-700 hover:border-blue-900 hover:shadow-lg hover:shadow-gray-500 text-white font-bold py-2 px-4 rounded
        />
      </div>
      <div col center>
        <label for="message" p="x4 y2" text="center" mx-8 mt-4 font-mono>Message</label>
        <div col m-4 mt-0 w-full center>
          <textarea
            id="message"
            v-model="message"
            rows="12"
            cols=" 60"
            placeholder="Your message, example: Hello, I'm interested in..."
            bg-blue-800 hover:bg-lime-300  hover:border-2 hover:border-blue-900 hover:shadow-lg hover:shadow-gray-500 hover:text-gray-700 text-white font-bold py-2 px-4 rounded
          ></textarea>
        </div>
      </div>
    </div>
    <input type="submit" value="Send" class="submit"
    
     w-full />
  </form>
  <Toast bg="lime-300" toast="Email sent successfully!" timeout="10" v-if="toast" />
</template>
<script setup lang="ts">
import { useUserStore } from "~/store/user";
import { Ref } from "vue";

const { api, getToken } = useUserStore();

const from = ref("");
const name = ref("");
const message = ref("");
const toast = ref(false);

const onSubmit = async () => {
  const body = {
    name: name.value,
    email: from.value,
    message: message.value,
  };
  const res = await fetch("/api/contact", {
    method: "POST",
    headers: {
     "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  })
  .then(res => res.json())
  toast.value = true;
  setTimeout(() => {
    toast.value = false;
  }, 10000);
}

</script>