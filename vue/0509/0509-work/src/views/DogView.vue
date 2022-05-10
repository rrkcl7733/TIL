<template>
<div>
  <button @click="showMeTheDog">show my dog</button>
  <img :src = "url">
</div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            url: ""
        }
    },
    methods: {
        showMeTheDog() {
            axios.get('https://api.thedogapi.com/v1/images/search/')
            .then(res => {
                this.url = res.data[0].url
            })
        }
    }
}
</script>

<style>

</style>