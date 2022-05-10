<template>
  <div class="about">
    <h2>{{ $route.params.num }}개 번호 추천!</h2>
    <button @click="getLuckyNums">눌러봐!</button>
    <p>{{ selectedNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: "LottoView",
  data() {
    return {
      selectedNums: ['^_^'],
    }
  },

  methods: {
    getLuckyNums() {
      this.selectedNums = _.sortBy(_.sampleSize(_.range(1, 46), this.$route.params.num))
    }
  }
}
</script>

