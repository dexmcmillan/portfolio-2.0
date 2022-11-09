<script setup>
  const { data: projects } = await useFetch('http://localhost:8000/api/projects/')
  console.log(projects)
</script>

<template>
  <div class="col-span-3">
    <div class="grid grid-cols-1 md:gap-10">
      <div class="col-span-4 pageTitle">work</div>
      <project-card v-for="project in projects" v-bind:key="project.id" v-bind:project="project" />
    </div>
  </div>
</template>

<script>
  export default {
    name: "StoriesPage",
  };
</script>

<style>
</style>
