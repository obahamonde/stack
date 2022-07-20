<script setup lang="ts">
import { useUserStore } from '@/store/user';
const {
    getToken,
    api
} = useUserStore();


const posts = ref([]);
const edit = ref(false);

onMounted(async () => {
    const token = await getToken();
    posts.value = await api.get(`/blog/${props.username}`, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    });
});

</script>

<template>
<div class="blog">
   

</div>
</template>
