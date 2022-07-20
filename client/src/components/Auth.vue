<template>
  <div m-4 br>
    <div v-if="isAuthenticated" row>
      <input
        type="text"
        outline
        slide-up
        rounded
        mx-16
        my-4
        text-gray-500
        text-sm
        p-1
        h-8
        br
        :class="{ hidden: chatInactive }"
        @keyup.enter="chat"
        v-model="message"
      />
      <div col :class="{ hidden: iconsActive }" slide-right>
        <Ico @click="logout" icon="mdi-logout" mb-1 text-red-500 shadow rf />
        <Ico
          @click="
            () => {
              profileActive = true;
              chatInactive = !chatInactive;
            }
          "
          mb-1
          icon="mdi-chat"
          shadow
          rf
          :class="{ active: !chatInactive }"
        />
        <Ico
          @click="
            () => {
              profileActive = !profileActive;
              chatInactive = true;
            }
          "
          mb-12
          shadow
          rf
          icon="mdi-account"
          :class="{ active: !profileActive }"
        />
      </div>

      <img
        :src="user.picture"
        rf
        x12
        br
        m-2
        shadow
        fixed
        z-50
        cp
        @click="iconsActive = !iconsActive"
      />
      <div
        :class="{ 'hidden': profileActive }"
        br
        m-4
        mx-16
        text-xs
        font-mono
        font-extrabold
      >
        <div bg-teal-500 p-1 rounded shadow slide-up>
          <h1 row-start>Username: {{ user.nickname }}</h1>
          <p row-start>Email: {{ user.email }}</p>
        </div>
      </div>
    </div>

    <div v-else>
      <Ico icon="mdi-account-circle" x12 @click="login" />
    </div>
  </div>
</template>
<style scoped>
.active {
  color: teal;
}
</style>
<script setup lang="ts">
import { useAuth0 } from "@auth0/auth0-vue";
import { useUserStore } from "~/store/user";
const { loginWithRedirect, user, isAuthenticated, logout, getAccessTokenSilently } = useAuth0();
import axios from "axios";

const store = useUserStore();

onBeforeMount(async () => {
  if (isAuthenticated) {
    const token = await getAccessTokenSilently();
    store.setToken(token);
    store.setUser(user._value);
  }

});




const chatInactive = ref(true);
const iconsActive = ref(true);
const profileActive = ref(true);


const message = ref("");

const login = async () => {
  try {
    loginWithRedirect();
} catch (error) {
    console.error(error);
  }
};

logout: () => {
  try {
    logout();
    setUser(null);
    setToken(null);
    isAuthenticated.value = false;
  } catch (error) {
    console.error(error);
  }
};

const chat = () => {
  const ws = new WebSocket("ws://localhost:8000/api/");
  ws.onopen = () => {
    ws.send(getToken());
    if (message.value) {
      console.log(message.value);
      ws.send(message.value);
      message.value = "";
    }
  };
  ws.onmessage = (event) => {
    alert(event.data);
  };
  ws.onclose = () => {
    console.log("disconnected");
  };
  ws.onerror = (error) => {
    console.log(error);
  };
};

onMounted(async()=>{
  const token = await getAccessTokenSilently();
  const response = await axios.get("http://localhost:3000/server/api", {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });
  console.log(response.data);
  store.setToken(token);
  store.setUser(response.data);
})


</script>
