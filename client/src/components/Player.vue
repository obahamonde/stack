<script setup lang="ts">
import AudioPlayer from "vue3-audio-player";
import "vue3-audio-player/dist/style.css";
</script>
<template>
  <div
    font-thin
    font-serif
    text-black
    col
    center
    tr
    m-8
    bg-teal
    dark:bg-amber
    p-8
    rf
    shadow
    fade-in-down
  >
    <AudioPlayer
      :option="{
        src: '/twi.mp3',
        title: '7 Nation Army',
        coverImage: '/logo.png',
        progressBarColor: '#00ff00',
        indicatorColor: '#000080',
      }"
      bg-gray-300
      rf
      shadow
      px-12
      py-2
    />
  </div>
</template>
