<script setup lang="ts">
import { ref, onMounted } from 'vue'
const props = defineProps<{endpoint:str}>()
const val = ref()
onMounted(
    async()=>{
    val.value = await fetch('/api/'+props.endpoint).then((res)=>res.json()) 
    })      
</script>
<template>
<p>
{{ val }}
</p>
</template>