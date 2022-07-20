import { acceptHMRUpdate, defineStore } from "pinia";
import { User } from "~/types";
import { Ref } from "vue";
import axios from "axios";

export const useUserStore = defineStore("user", () => {
  const currentUser: Ref<User | null> = ref(
    null
  );
  const token: Ref<string | null> = ref(null);
  const client = ref(axios.create({
    baseURL: "http://localhost:3000/server/api",
    headers: {
      Authorization: `Bearer ${token.value}`,
    },
  })); 
  function setUser(u: User | null) {
    currentUser.value = u;
  }
  function getUser(): User | null {
    return currentUser.value;
  }

  function setToken(t: any | null) {
    token.value = t;
    }
    function getToken(): string | null {
        return token.value;
    }

  function setClient(c: any) {
    client.value = c;
  }
  function getClient(): any {
    return client.value;
  }

  
  return {
    setUser,
    getUser,
    currentUser,
    setToken,
    getToken,
    token,
  client,
setClient,
getClient  };  
})

if(import.meta.hot)
  import.meta.hot.accept(acceptHMRUpdate(useUserStore, import.meta.hot));
