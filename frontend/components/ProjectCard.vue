<template>
    <div>
      <div class="flex my-1">
        <TagTab v-for="tag in project.tags" v-bind:key="tag.id" :tag="tag" />
      </div>
      <h2 id="ideaHeader"><a :href="project.link" target="_blank">{{ project.title }}</a></h2>
      <span style="opacity:0.8">{{ project.publication }}<span v-if="project.publication"> / </span>{{ $format_date(project.date) }}</span>
      <p class="ideaBody mt-3" v-html="project.description"></p>
      <div v-if="project.embed" v-html="project.embed" class="p-2 md:px-5"></div>
      <div v-if="project.picture" class="p-2 md:px-5"><img :src="project.picture" /></div>
  </div>
</template>

<script>
  export default {
    name: 'ProjectCard',
    props: ['project'],
    
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h2 {
  font-size: 24pt;
  font-weight:bold;
}



</style>
