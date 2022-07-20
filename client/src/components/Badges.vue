<template>
  <div
    slide-down
    row
    bg-transparent
    dark:bg-transparent
    top-0
    w-full
    justify-center
    mr-40
    h-16
    fixed


  >
    <Ico icon="logos:vue" m-2 x12 rf shadow 
      @click="demo3 = !demo3" 
    />
    <Ico icon="logos:tailwindcss-icon" m-2 x12 rf shadow 
      @click="demo2=!demo2"
    />
    <Ico icon="logos:typescript-icon" m-2 x12 rf shadow />
    <Ico icon="logos:python" m-2 x12 rf shadow />
    <Ico icon="simple-icons:fastapi" text-teal-700 m-2 x12 rf shadow />
    <Ico icon="logos:flask" text-teal-700 m-2 x12 rf shadow />
    <Ico icon="logos:oauth" m-2 x12 rf shadow />
    <Ico icon="logos:linux-tux" m-2 x12 rf shadow />
    <Ico icon="logos:docker-icon" m-2 x12 rf shadow />
    <Ico icon="logos:aws" m-2 x12 rf shadow />
    <Ico icon="logos:google-cloud" m-2 x12 rf shadow @click="demo = !demo" />
    <Ico icon="simple-icons:fauna" text-purple-900 m-2 x12 rf shadow />
    <Ico icon="logos:postgresql" m-2 x12 rf shadow />
  </div>
  <div v-if="demo" tr bg-gray-300 mr-20 p-2 mt-20>
    <div shadow-2xl bg-gray-200>
      <strong text-teal-700 font-extrabold text-2xl underline>CloudChat</strong>
      <p w-100 p-4 rounded-lg shadow>
        A chat Application made with VueJS, Javascript, TailwindCSS taking advantage of
        the real time database feature from Google Firestore and using Google Social Login
        as Authentication Method
        <a href="https://cloudchat.netlify.app/" target="_blank">
          <div row>
            <Ico icon="logos:netlify" text-teal-700 m-2 x12 rf shadow /><span m-4 underline font-bold>Hosted in Netlify</span>
          </div>
        </a>
      </p>
    </div>
  </div> <div v-if="demo2" tl bg-gray-300 ml-20 p-2 mt-20>
    <div shadow-2xl bg-gray-200>
      <strong text-teal-700 font-extrabold text-2xl underline>Resume</strong>
      <p w-100 p-4 rounded-lg shadow>
        A cookie cutter resume made with TailwindCSS and plain HTML.
        <a href="https://cv-ob.netlify.app" target="_blank">
          <div row>
            <Ico icon="logos:netlify" text-teal-700 m-2 x12 rf shadow /><span m-4 underline font-bold>Hosted in Netlify</span>
          </div>
        </a>
      </p>
    </div>
  </div>
  <div v-if="demo3" tl bg-gray-300 ml-20 p-2 mt-20>
    <div shadow-2xl bg-gray-200>
      <strong text-teal-700 font-extrabold text-2xl underline>Vuenyl</strong>
      <p w-100 p-4 rounded-lg shadow>
        A VueJS E-Commerce Application
        <a href="https://vuenyl.netlify.app" target="_blank">
          <div row>
            <Ico icon="logos:netlify" text-teal-700 m-2 x12 rf shadow /><span m-4 underline font-bold>Hosted in Netlify</span>
          </div>
        </a>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
const demo = ref(false);
const demo2 = ref(false);
const demo3 = ref(false);
</script>
