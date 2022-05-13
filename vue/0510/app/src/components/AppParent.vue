<template>
  <div>
    <input type="text" v-model="parentData"
    @keyup="parent">
    <h4>appData : {{ msg }}</h4>
    <h4>childData : {{ childData }}</h4>
    <hr>
    <app-child :msg="parentData" :msgg="msg"
    @child-show="childGet"></app-child>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'
export default {
  components: {
    AppChild
  },
  props: {
    msg: String
  },
  data() {
    return {
      parentData: '',
      childData: ''
    }
  },
  methods: {
    parent() {
      this.$emit('parent-show', this.parentData, this.childData)
    },
    childGet(inputData) {
      this.childData = inputData
    },
  }
}
</script>

<style>

</style>