<template>
  <div v-if="video" class="video-detail">
    <iframe :src="videoURI" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  props: {
    video: Object,
  },
  computed: {
    videoURI() {
      const videoId = this.video.id.videoId
      return `http://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>