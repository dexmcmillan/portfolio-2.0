<script setup>
  const { data: tags } = await useFetch(`https://d45esux869ize.cloudfront.net/api/tags/`);
  const shown = await useShown()

  console.log(shown)

  const props = defineProps({tag: Object})

  const { tag } = toRefs(props);

  const change_view = () => {
    console.log(shown.value)

    if (shown.value.includes(tag.value.name)) {
      shown.value = shown.value.filter(i => i != tag.value.name)
      console.log("Shown will not change.")
    }
    else {
      shown.value.push(tag.value.name)
      console.log("Shown should be changed.")
    }
  }

  const active = computed(() => {
    if (shown.value.includes(tag.value.name)) {
        return true
    }
    else {
        return false
    }
  })

</script>

<template>
  <div :class="{ 'tag-active': active, 'tag-inactive': !active}" class="tag tag-active p-1" @click="change_view">
    {{ tag.name }}
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
