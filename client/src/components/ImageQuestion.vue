<template>
  <div v-if="imagehash">
    <h3>Is this a photo or computer graphics?</h3>
    <img class="questionimage" :src="url" @load="loaded()"/>
    <button type="button" class="saw-button" @click="seen">I have already seen this!</button>

    <div class="buttons">
      <button type="button" class="cg-button" @click="cg" ref="cgbutton">Computer graphics</button>
      <button type="button" class="photo-button" @click="photo" ref="photobutton">Photo</button>
    </div>
  </div>
</template>

<script>
export default{
  props: {
    imagehash: ''
  },
  data: function () {
    return {
      start: null
    }
  },
  mounted () {
    this.start = new Date()
  },
  watch: {
    imagehash: function () {
      this.start = new Date()
    }
  },
  computed: {
    url: function () {
      return '/api/images/' + this.imagehash
    }
  },
  methods: {
    cg: function () {
      this.loading()
      this.$emit('answered', { result: 'cg', duration: this.get_duration() })
    },
    photo: function () {
      this.loading()
      this.$emit('answered', { result: 'photo', duration: this.get_duration() })
    },
    seen: function () {
      this.loading()
      this.$emit('answered', { result: 'seen', duration: this.get_duration() })
    },
    get_duration () {
      return (new Date().getTime() - this.start.getTime()) / 1000
    },
    loading: function () {
      this.$refs.cgbutton.disabled = true
      this.$refs.photobutton.disabled = true
    },
    loaded: function () {
      this.$refs.cgbutton.disabled = false
      this.$refs.photobutton.disabled = false
    }
  }
}
</script>
<style type="sass">
  .questionimage{
    max-width: 100vw;
    max-height: 90vh;
  }
  .buttons{
    position: absolute;
    bottom: 20px;
    width: 100%;
  }
  .cg-button{
    float: left;
    margin-left: 30px;
  }
  .photo-button{
    margin-right: 30px;

  float: right;
}

button:disabled{
  background-color: grey;
}

  .saw-button{
      position: absolute;
    top: 8px;
    right: 8px;
    background-color: lightgrey;
    color: black;
}
</style>
