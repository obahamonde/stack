<script setup lang="ts">
import { Icon } from "@iconify/vue";
const props = defineProps<{
  icon: str;
}>();
</script>
<template>
  <Icon :icon="icon" hover:scale-125 cursor-pointer transition-all ease-in-out />
</template>
