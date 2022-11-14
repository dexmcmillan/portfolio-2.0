<script setup>
  const { data: jobs } = await useFetch('https://data.dextermcmillan.com/api/jobs/')
  const { data: tags } = await useFetch(`https://data.dextermcmillan.com/api/tags/`);
  const shown = await useShown()

  const filtered_jobs = computed(() => jobs.value.filter((x) => x.tags.map(x => x.name).some(r=> shown.value.includes(r))))
</script>

<template>
  <div class="col-span-3 grid grid-cols-4 md:gap-10 mb-7">
    <div class="col-span-4 pageTitle">resumé</div>
    <!-- <div v-if="filtered_jobs.length <= 0">There's nothing here! Please choose tags on the left to display work in that category.</div> -->
    <TransitionGroup name="list">
      <job-card v-for="job in filtered_jobs" v-bind:key="job.id" v-bind:job="job"/>
    </TransitionGroup>
  </div>
</template>

<style>

</style>
