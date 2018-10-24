<template>
  <div class="question">
    <h3>{{question}}</h3>
    <label v-for="a in answers" :key="a">
      <input  type="radio" name="answer" :value="a" v-model="choice"/>
      {{a}}
    </label>
    <button @click="next" type="button">Next</button>
  </div>
</template>
<script>
export default{
  props: {
    question: '',
    answers: {
      type: Array,
      default: () => []
    }
  },
  data: function () {
    return {
      choice: ''
    }
  },
  mounted () {
    this.choice = ''
  },
  methods: {
    next: function () {
      this.$emit('answered', this.choice)
    }
  }
}
</script>
<style>
  label{
    display: block;
    text-align: left;
  }
  .question{
    width: 100%;
    max-width: 500px;
    margin: auto auto;
  }
</style>
