<template>
<transition>
<h1 
:class="{
  'slideInRight': (timer>timeout) ? true : false,
}

"
:bg="props.bg" 
 py-2 px-4 rounded shadow-lg
tr mt-16 row
invert
dark:filter-none
dark:text-black

>{{toast}}<Ico icon="mdi-close" m-1 ml-2 rf shadow-md shadow-gray-500 cursor-pointer 

@click="timer=999"

 /></h1></transition>
</template>

<script setup lang="ts">
var timer = ref(0);
const interval = setInterval(() => {
  timer.value++;
}, 1000);
const props = defineProps<{
  timeout: number;
    bg: string;
    toast:string
}>()
</script>