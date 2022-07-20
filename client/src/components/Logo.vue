<template>
<div col center>
<img :src="logo" x12 rf  />
</div></template>
<script setup lang="ts">
defineProps<{
  logo: string
}>()
</script>