<template>
  <div>
    <input type="text" @keyup.enter="onInputKeyword" v-model="keyword" placeholder="검색어를 입력하세요.">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      keyword: null,
    }
  },
  methods: {
    onInputKeyword() {
      this.$emit("input-change", this.keyword)
    }
  }
}
</script>

<style>

</style>