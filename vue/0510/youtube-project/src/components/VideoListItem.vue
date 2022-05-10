<template>
  <div @click="selectVideo" class="video-item">
    <img :src="video.snippet.thumbnails.medium.url">
    <div class="video-description">
      <h3>{{ video.snippet.title }}</h3>
      <p>{{ video.snippet.description }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    video: {
      type: Object,
      required: true,
    }
  },
  methods: {
    selectVideo() {
      this.$emit('select-video', this.video)
    }
  }
}
</script>

<style scoped>
.video-item {
  display: flex;
  margin-bottom: 1rem;
  border: 1px solid gray;
}

.video-description {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  text-align: left;
}
</style>
