<template>
<div v-if="bucket">  <a :href="'http://'+JSON.parse(bucket).bucket_url" btn bg-amber outline hover:invert   >
    Visit Webpage
  </a></div>

  <textarea code rows="12" cols="96" outline
    v-model="code"
    rounded
    bg-black
    p-2
    m-4
    placeholder = 'Paste your code here, then click "Create Webpage" to deploy

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><!-- Write an awesome title! --></title>
    <style>
        /* Write your styles here! */
    </style>
</head>
<body>
    <!-- Write your html code here -->
    <script>
    // Write your script here!
    </script>
</body>
</html>
'
    text-lime-300
    @keydown.ctrl.enter="run"
  >
  </textarea>
  <button btn-primary @click="run">Create Webpage</button>
</template>

<script setup lang="ts">
const code = ref()
const bucket = ref(null)
const url = ref(null)
import { useUserStore} from '~/store/user'

const { api, getToken } = useUserStore()

  async function run() {
    const res = await api.post('/bucket/?content=' + encodeURIComponent(code.value), {}, {
      headers: {
        Authorization: 'Bearer ' + getToken()
      }
    })	
    bucket.value = JSON.parse(res.data)
  }
</script>