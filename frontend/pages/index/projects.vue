<script setup>
  const { data: projects } = await getProjects()
  const shown = await useShown()

  const filtered_projects = computed(() => projects.value.filter((x) => x.tags.map(x => x.name).some(r=> shown.value.includes(r))))

</script>

<template>
  <div class="col-span-3">
    <div class="grid grid-cols-1 md:gap-10 gap-5">
      <div class="col-span-4 pageTitle">work</div>
      
      <TransitionGroup name="list">
        <project-card v-for="project in filtered_projects" v-bind:key="project.id" v-bind:project="project" />
      </TransitionGroup>
      <!-- <div v-if="filtered_projects.length <= 0">There's nothing here! Please choose tags on the left to display work in that category.</div> -->
    </div>
  </div>
</template>

<style>

</style>
