<script setup>
  const { data: tags } = await useFetch(`https://d45esux869ize.cloudfront.net/api/tags/`);
</script>

<template>
    <div id="app">
      <Header class=""></Header>
      <div></div>
      <NuxtPage class="lg:pl-20 text-left" />
    </div>
  </template>
  
  <style>
  </style>
  