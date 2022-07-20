<script setup lang="ts">
import { Icon } from "@iconify/vue"
const props = defineProps<{logo:string}>()
</script>
<template>
<Icon :icon="props.logo" />
</template>