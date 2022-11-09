<script setup>
  const shown = useState('shown')
</script>


<template>
  <div :class="{ 'tag-active': active, 'tag-inactive': !active}" class="tag p-1" @click="change_view(tag.name)">
    {{ tag.name }}
  </div>
</template>

<script> 
  export default {
    name: 'Header',
    props: ['tag'],
    methods: {
      change_view: function (name) {

        console.log("Start!")
        console.log(this.shown)

        if (this.shown.includes(name)) {
          this.shown = this.shown.filter(i => i != name)
          console.log("Shown will not change.")
        }
        else {
          this.shown.push(name)
          console.log("Shown should be changed.")
        }
        
        console.log(this.shown)
      }
    },
    computed: {
        active() {
            if (this.shown.includes(this.tag.name)) {
                return true
            }
            else {
                return false
            }
        }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
