<template>
  <div tr m-8 fade-in-down>
    <div class="dropzone-container">
      <input
        type="file"
        id="files"
        name="files"
        ref="files"
        multiple
        accept="image/*"
        enctype="multipart/form-data"
        @change="handleFiles"
        hidden
      />
      <label for="files" class="dropzone">
        <div v-if="fileList.length > 0">
          <Icon
            icon="mdi-delete"
            @click.prevent="fileList = []"
            right-2
            top-2
            hover:text-red-500
            cursor-pointer
          />
        </div>
        {{ fileList.length > 0 ? fileList.length + " files selected" : "Upload Images" }}
        <div v-if="fileList.length > 0" col center>
          <Ico icon="mdi-upload" class="upload_icon" @click.prevent="uploadFiles" />
        </div>
      </label>
    </div>
  </div>
  <div class="preview-container">
    <div
      v-for="file in fileList"
      bg-cyan
      shadow
      rounded-lg
      p-2
      m-2
      w-32
      h-44
      col
      justify-start
    >
      <div col items-center>
        <Ico
          icon="mdi-delete"
          @click="removeFile(file)"
          text
          ml-26
          hover:text-red-500
          cursor-pointer
        />
        <h1 text-xs font-bold text-center font-sans>
          {{ file.name }}
        </h1>
        <h2 text-xs text-center font-serif>
          {{ new Date(file.lastModified).toLocaleString() }}
        </h2>
      </div>
      <div>
        <h2 text-xs text-center font-mono>
          {{
            file.size < 1024 * 1024
              ? (file.size / 1024).toFixed(2) + "KB"
              : (file.size / 1024 / 1024).toFixed(2) + "MB"
          }}
        </h2>
        <h3 text-xs text-center font-sans>
          {{ file.type }}
        </h3>
        <div>
          <div col items-center v-if="file.type.startsWith('image')">
            <img :src="file.preview" x20 />
          </div>
          <div col items-center v-else>
            <Icon icon="mdi-file" w-32 h-32 />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dropzone-container {
  @apply flex justify-center h-full;
}
.dropzone {
  @apply h-32 w-48 bg-teal col center;
  @apply rounded shadow-lg shadow-gray-500;
  @apply hover:border-2 hover:border-black hover:border-dashed;
  @apply hover:cursor-pointer hover:bg-white hover:shadow-black hover:text-black;
  @apply transition-all duration-200 ease-in-out;
  @apply text-md;
}
.upload_icon {
  @apply h-12 w-12 
  @apply text-black border-2 border-black;
  @apply hover:scale-125 hover:transition-all hover:ease-in-out 
  @apply cursor-pointer rounded-full;
  @apply mt-4;
  @apply hover:bg-black hover:text-white;
}
</style>
<script setup lang="ts">
import axios from "axios";
import { useAuth0 } from "@auth0/auth0-vue";
const store = useUserStore();
const fileList = ref([]);
const responses = ref([]);
const token = ref();
const { user, isAuthenticated, getAccessTokenSilently } = useAuth0();
const handleFiles = (e: Event) => {
  Array.from(e.target.files || []).forEach((file) => {
    const reader = new FileReader();
    reader.onload = (e: ProgressEvent) => {
      fileList.value.push({
        name: file.name,
        lastModified: file.lastModified,
        size: file.size,
        type: file.type,
        preview: e.target.result,
        file: file,
      });
    };
    reader.readAsDataURL(file);
  });
};
const removeFile = (file: File) => {
  fileList.value = fileList.value.filter((f) => f !== file);
};
const uploadFiles = () => {
  fileList.value.forEach(async (file) => {
    const formData = new FormData();
    formData.append("file", file.file);
    const response = await fetch(`/server/upload/${await getAccessTokenSilently()}`, {
      method: "POST",
      body: formData,
    });
    const data = await response.json();
    console.log(data);
    responses.value.push(data);
  });
};

onBeforeMount(async () => {
  if (isAuthenticated) {
    const token = await getAccessTokenSilently();
    store.setToken(token);
    store.setUser(user._value);
  }
});

onMounted(async () => {
  const response = await fetch(`/server/upload/${await getAccessTokenSilently()}`);
  const data = await response.json();
  console.log(data);
});
</script>
