<script setup>
  const { data: jobs } = await useFetch('http://localhost:8000/api/jobs/')
</script>

<template>
  <div class="col-span-3 grid grid-cols-4 md:gap-10 mb-7">
    <div class="col-span-4 pageTitle">resumé</div>
    <job-card v-for="job in jobs" v-bind:key="job.id" v-bind:job="job"/>
  </div>
</template>

<script>

export default {
  name: "AboutPage",
}
</script>

<style>
</style>
