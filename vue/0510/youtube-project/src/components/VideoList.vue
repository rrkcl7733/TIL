<template>
  <ul>
    <VideoListItem v-for="video in videos" 
      :key="video.id.videoId" 
      :video="video"
      @select-video="onSelectVideo"/>
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
      required: true,
    }
  },
  methods: {
    onSelectVideo(video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>