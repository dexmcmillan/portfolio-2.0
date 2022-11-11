<script setup>
  const { data: tags } = await useFetch(`http://35.183.248.100/api/tags/`);
  const { data: projects } = await useFetch(`http://35.183.248.100/api/projects/`)
  const shown = useState('shown')
</script>

<template>
  <div class="col-span-3">
    <div class="grid grid-cols-1 md:gap-10">
      <div class="col-span-4 pageTitle">work</div>
      
      <TransitionGroup name="list">
        <project-card v-for="project in filtered_projects" v-bind:key="project.id" v-bind:project="project" />
      </TransitionGroup>
      <!-- <div v-if="filtered_projects.length <= 0">There's nothing here! Please choose tags on the left to display work in that category.</div> -->
    </div>
  </div>
</template>

<script>
  export default {
    name: "StoriesPage",
    computed: {
      filtered_projects () {
        return this.projects.filter((x) => x.tags.map(x => x.name).some(r=> this.shown.includes(r)))
      },
    }
  }
</script>

<style>

</style>
