<script setup lang="ts">

useHead({
  title: 'CloudApp',
  meta: [
    { name: 'description', content: 'Fast API Vue JS Cloud Template' },
    {
      name: 'theme-color',
      content: computed(() => isDark.value ? '#00aba9' : '#ffffff'),
    },
  ],
  link: [
    {
      rel: 'icon',
      type: 'image/png',
      href: '/logo.png'
    },
  ],
})
</script>

<template>
  <main font-sans  text="center gray-700 dark:gray-200" col center>
    <router-view />
  </main>
</template>
