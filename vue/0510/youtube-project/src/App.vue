<template>
  <div id="app">
    <SearchBar @input-change="onInputChange"/>
    <VideoDetail :video="selectedVideo"/>
    <VideoList :videos="videos"
    @select-video="onVideoSelect"/>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return {
      inputValue: null,
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    onInputChange(keyword) {
      this.inputValue = keyword
      axios({
        method: 'get',
        url: API_URL,
        params: {
          part: 'snippet',
          type: 'video',
          key: API_KEY,
          q: this.inputValue
        }
      })
      .then(res => {
        this.videos = res.data.items
      })
      .catch(err => console.log(err))
    },
    onVideoSelect(video) {
      this.selectedVideo = video
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
