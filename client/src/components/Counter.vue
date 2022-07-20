<script setup lang="ts">
import { ref } from 'vue'
import { Icon } from '@iconify/vue'
const props = defineProps<{stock:number}>()
const count = ref(0)
const inc = ()=>{
    (count.value<props.stock) ? count.value++ : count.value=props.stock
}
const dec = ()=>{
    (count.value>0) ? count.value-- : count.value=0
    }
</script>
<template>
<div row items-center>
<Icon icon="mdi-minus"
    @click="dec()"
    font-mono
/>
<span   font-serif
        text-lg 
>{{count}}</span>
<Icon icon="mdi-plus"
    @click="inc()"
    font-mono
/>
</div>
</template>