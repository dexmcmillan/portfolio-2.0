<script setup>
  const { data: tags } = await useFetch(`http://35.183.248.100/api/tags/`);
  const shown = useState('shown', () => tags.value.map(x => x.name))
</script>

<template>
    <div id="app">
      <Header class=""></Header>
      <div></div>
      <NuxtPage class="lg:pl-20 text-left" />
    </div>
  </template>
  
  <script>
  
  export default {
    name: "AboutPage",
  }
  </script>
  
  <style>
  </style>
  