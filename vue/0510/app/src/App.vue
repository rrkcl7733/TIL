<template>
  <div id="app">
    <input type="text" v-model="appData">
    <h4>parentData : {{ parentData }}</h4>
    <h4>childData : {{ childData }}</h4>
    <hr>
    <app-parent :msg="appData"
    @parent-show="parentGet"
    @child-show="childGet">
    </app-parent>
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent
  },
  data() {
    return {
      appData: '',
      parentData: '',
      childData: ''
    }
  },
  methods: {
    parentGet(inputData, inputtData) {
      this.parentData = inputData
      this.childData = inputtData
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
