<script setup>

  const props = defineProps({pictures: Array})
  
</script>

<template>
    <div class="grid grid-cols-1 gap-3">
      <img v-for="picture in pictures" :key="picture.id" :src="picture.file" />
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  h2 {
    font-size: 24pt;
    font-weight:bold;
  }

</style>
