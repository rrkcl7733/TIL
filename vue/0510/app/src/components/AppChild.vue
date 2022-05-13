<template>
  <div>
    <input type="text" v-model="childData"
    @keyup="child">
    <h4>appData : {{ msgg }}</h4>
    <h4>parentData : {{ msg }}</h4>
    <h4>childData : {{ childData }}</h4>
  </div>
</template>

<script>
export default {
  props: {
    msg: String,
    msgg: String,
  },
  data() {
    return {
      childData: ''
    }
  },
  methods: {
    child() {
      this.$emit('child-show', this.childData)
    }
  }
}
</script>

<style>

</style>