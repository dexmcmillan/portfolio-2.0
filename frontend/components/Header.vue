<script setup>
  const { data: tags } = await getTags()
</script>


<template>
  <div class="lg:fixed lg:w-1/4 h-full mb-10">
    <div id="socials" class="text-left py-1">
      <a href="http://www.twitter.com/dexmcmillan" target="_blank" class="pr-1"><v-icon>mdi-twitter</v-icon></a>
      <a href="http://www.instagram.com/dexmcmillan" target="_blank" class="pr-1"><v-icon>mdi-instagram</v-icon></a>
      <a href="https://www.linkedin.com/in/dexmcmillan" target="_blank" class="pr-1"><v-icon>mdi-linkedin</v-icon></a>
      <a href="https://www.github.com/dexmcmillan" target="_blank" class="pr-1"><v-icon>mdi-github</v-icon></a>
    </div>
    <nuxt-link to="/"><h1 id="title" class="py-1">Dexter McMillan</h1></nuxt-link>
    <div id="subtitle" class="py-1">
      <nuxt-link to="/resume" style="opacity:0.5">resumé</nuxt-link> / 
      <nuxt-link to="/projects" style="opacity:0.5">work</nuxt-link>
    </div>
    <div class="py-1 hidden sm:block">
      <p id="bio">Two-time RTDNA award-winning journalist, data analyst, web developer, and Datawrapper enthusiast.</p>
    </div>
    <div>
      <TagTab v-for="tag in tags" v-bind:key="tag.id" :tag="tag" />
    </div>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  #bio {
    line-height:140%;
  }

</style>
