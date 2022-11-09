<script setup>
  const { data: tags } = await useFetch(`http://localhost:8000/api/tags/`);
</script>


<template>
  <div class="lg:fixed lg:w-1/4 h-full mb-10">
    <div id="socials" class="text-left py-1">
      <a href="http://www.twitter.com/dexmcmillan" target="_blank" class="pr-1"><v-icon class="my-1">mdi-twitter</v-icon></a>
      <a href="http://www.instagram.com/dexmcmillan" target="_blank" class="pr-1"><v-icon class="my-1">mdi-instagram</v-icon></a>
      <a href="https://www.linkedin.com/in/dexmcmillan" target="_blank" class="pr-1"><v-icon class="my-1">mdi-linkedin</v-icon></a>
      <a href="https://www.github.com/dexmcmillan" target="_blank" class="pr-1"><v-icon class="my-1">mdi-github</v-icon></a>
    </div>
    <nuxt-link to="/"><h1 id="title" class="py-1">Dexter McMillan</h1></nuxt-link>
    <div id="subtitle" class="py-1">
      <nuxt-link to="/resume" style="opacity:0.5">resumé</nuxt-link> / 
      <nuxt-link to="/projects" style="opacity:0.5">work</nuxt-link>
    </div>
    <div class="py-1 hidden sm:block">
      <p id="bio">Two-time RTDNA award-winning journalist, data analyst, Datawrapper enthusiast, and web developer.</p>
    </div>
    <div>
      <TagTab v-for="tag in tags" v-bind:key="tag.id" :tag="tag" />
    </div>
  </div>
</template>

<script> 
  export default {
    name: 'Header',
      
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  #bio {
    line-height:140%;
  }

</style>
