<script setup>
  const { data: jobs } = await useFetch('http://localhost:8000/api/jobs/')
  const shown = useState('shown')
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

<script>

export default {
  name: "AboutPage",
  computed: {
    filtered_jobs () {
      const filtered = this.jobs.filter((x) => x.tags.map(x => x.name).some(r=> this.shown.includes(r)))

      return filtered
    },
    }
}
</script>

<style>

</style>
