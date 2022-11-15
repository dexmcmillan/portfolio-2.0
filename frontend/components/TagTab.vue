<template>
  <div :class="{ 'tag-active': active, 'tag-inactive': !active}" class="tag tag-active p-1" @click="change_view">
    {{ tag.name }}
  </div>
</template>

<script setup>

  // Get data from the tags table of our database.
  const { data: tags } = await getTags()
  
  // Load in the list of shown tags from state.
  const shown = await useShown()

  // Define props list, which is just the tag passed to the TagTab.
  const props = defineProps({tag: Object})

  const { tag } = toRefs(props);

  const change_view = () => {

    if (shown.value.includes(tag.value.name)) {

      shown.value = shown.value.filter(i => i != tag.value.name)

      console.log("Shown will not change.")

    }

    else {

      shown.value.push(tag.value.name)

      console.log("Shown should be changed.")

    }

  }

  // This is a computed property that controls whether the button is dark blue (active) or light (deactive).
  const active = computed(() => {
    // If the tag name in this button is included in the shown list...
    if (shown.value.includes(tag.value.name)) {

        // ...it is active.
        return true

    }

    else {
        // ...otherwise, it is not.
        return false

    }

  })

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
