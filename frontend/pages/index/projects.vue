<script setup>
  const { data: tags } = await useFetch(`http://localhost:8000/api/tags/`);
  const { data: projects } = await useFetch(`http://localhost:8000/api/projects/`)
  const shown = useState('shown')
</script>

<template>
  <div class="col-span-3">
    <div class="grid grid-cols-1 md:gap-10">
      <div class="col-span-4 pageTitle">work</div>
      <project-card v-for="project in filtered_projects" v-bind:key="project.id" v-bind:project="project" />
    </div>
  </div>
</template>

<script>
  export default {
    name: "StoriesPage",
    computed: {
      filtered_projects () {
        console.log("Shown projects are updated!")
        console.log(this.shown)
        // const filtered = this.projects.filter((x) => x.tags.map(x => x.name).includes("audio"))
        const filtered = this.projects.filter((x) => x.tags.map(x => x.name).some(r=> this.shown.includes(r)))
        console.log(filtered)

        return filtered
      },
    }
  }
</script>

<style>
</style>
