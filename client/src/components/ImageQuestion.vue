<template>
  <div v-if="imagehash">
    <h3>Is this a photo or computer graphics?</h3>
    <img class="questionimage" :src="url"/>
    <button type="button" class="saw-button" @click="seen">I have already seen this!</button>

    <div class="buttons">
      <button type="button" class="cg-button" @click="cg">Computer graphics</button>
      <button type="button" class="photo-button" @click="photo">Photo</button>
    </div>
  </div>
</template>

<script>
export default{
  props: {
    imagehash: ''
  },
  computed: {
    url: function () {
      return '/api/images/' + this.imagehash
    }
  },
  methods: {
    cg: function () {
      this.$emit('answered', 'cg')
    },
    photo: function () {
      this.$emit('answered', 'photo')
    },
    seen: function () {
      this.$emit('answered', 'seen')
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

  .saw-button{
      position: absolute;
    top: 8px;
    right: 8px;
    background-color: lightgrey;
    color: black;
}
</style>
