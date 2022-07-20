<template>
  <div>
    <nav text-xl mt-4 inline-flex gap-2 tl ml-4 fixed fade-in-left>
      <button icon-btn @click="toggleDark()" style="background: #000080" p-1 rf>
        <div dark:i-carbon-moon i-carbon-sun text-white />
      </button>
      <router-link to="/" mt-24 m-1 text-2xl fixed>
        <Ico icon="mdi-home" text-teal />
      </router-link>
      <router-link to="/about" mt-32 m-1 text-2xl fixed>
        <Ico icon="mdi-information" text-teal />
      </router-link>
      <router-link to="/contact" mt-40 m-1 text-2xl fixed>
        <Ico icon="mdi-email" text-teal />
      </router-link>
      <router-link to="/blog" mt-48 m-1 text-2xl fixed>
        <Ico icon="mdi-post" text-teal />
      </router-link>
      <router-link to="/images" mt-56 m-1 text-2xl fixed>
        <Ico icon="mdi-image" text-teal />
      </router-link>
      <router-link to="/demo" mt-64 m-1 text-2xl fixed>
        <Ico icon="mdi-cloud" text-teal />
      </router-link>
      <router-link to="/music" mt-72 m-1 text-2xl fixed>
        <Ico icon="mdi-music" text-teal />
      </router-link>
      <Auth />
    </nav>
  </div>
</template>
