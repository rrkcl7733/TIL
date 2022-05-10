<template>
  <div class="lunch">
    <img alt="Vue logo" src="../assets/logo.png">
    <h2>점심메뉴</h2>
    <button @click="choiceMenu">Pick Lunch</button>
    <p class="menu">점심 메뉴는???</p><br>

    <h3>{{ menu }}   !!!</h3>
    <h2>로또 뽑으러 가자</h2>
    <button @click="moveToLotto">Pick Lotto</button>
  </div>
</template>

<script>
// @ is an alias to /src
import _ from 'lodash'
export default {
  name: "MyLunch",
  data() {
    return {
      menus: ['납작만두', '볶음밥'],
      menu: ''
    }
  },
  methods: {
    moveToLotto() {
      this.$router.push({ name: 'LottoView', params: { num: '6' } })
    },
    choiceMenu() {
      this.menu = _.sample(this.menus)
    }
  }

}
</script>
