<template>
  <div class="col-span-auto col-span-full grid grid-cols-4 md:gap-10 mb-7">

      <div class="col-span-4 md:col-span-1">

        <h2 class="md:text-right">{{ job.org }}</h2>

        <!-- This is the mobile version.-->
        <div class="sm:hidden">
          <p v-if="job.date_from" class="md:text-right">{{ job.title }} / <i>{{ $format_job_date(job.date_from) }} - <span v-if="!job.current">{{ $format_job_date(job.date_to) }}</span><span v-if="job.current">Present</span></i></p>
        </div>

        <!-- This is the desktop version version.-->
        <div class="hidden sm:block">
          <p class="md:text-right">{{ job.title }}<br>
          <span v-if="job.date_from" class="md:text-right"><i>{{ $format_job_date(job.date_from) }} - <span v-if="!job.current">{{ $format_job_date(job.date_to) }}</span><span v-if="job.current">Present</span></i></span></p>
        </div>

      </div>

      <div class="col-span-4 md:col-span-3">

        <ul v-html="job.accomplishments">
        </ul>

      </div>

  </div>
</template>

<script>
export default {
  name: 'JobCard',
  props: ['job'],
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h2 {
  font-size: 14pt;
  font-weight:bold;
}

</style>
