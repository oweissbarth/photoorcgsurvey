<template>
<div class="survey">
<progress :value="current_img" max="49"></progress>
<single-choice-question v-if="!metaDone && !done" :question="meta[current_meta].question" :answers="meta[current_meta].answers" @answered="handle_answered_meta"/>
<image-question v-if="metaDone && !done" :imagehash="images[current_img]._id" @answered="handle_answered_image"/>
<done v-if="done" :correct="correct" :total="total" :results="results"></done>
</div>
</template>
<script>
import ImageQuestion from '../components/ImageQuestion.vue'
import SingleChoiceQuestion from '../components/SingleChoiceQuestion.vue'
import Done from '../components/Done.vue'
export default{
  components: {
    ImageQuestion,
    SingleChoiceQuestion,
    Done
  },
  data: function () {
    return {
      meta: [
        { tag: '3d-software', question: 'How often do you use 3D-graphics-software (Blender, UE4, Modo, ZBrush, etc...)?', answers: ['Never', 'Once a month', 'Once a week', 'Multiple times a week', 'Everyday'] },
        { tag: 'games', question: 'How much time do you spend per week playing computer/console games ', answers: ['less then 1h', '1-3h', '3-6h', '6-12h', 'more than 12h'] }
      ],
      current_meta: 0,
      images: [],
      current_img: 0,
      answers: {},
      metaDone: false,
      done: false,
      correct: 0,
      total: 0,
      results: [],
      timestart: null,
      timeend: null,
      ticket: null
    }
  },
  mounted () {
    if (localStorage.ticket) {
      this.ticket = localStorage.ticket
    } else {
      fetch('/api/ticket').then(res => res.json()).then(res => { this.ticket = res['ticket']; localStorage.ticket = res['ticket'] })
    }
    fetch('/api/').then(res => res.json()).then(res => { this.images = res })
    this.timestart = new Date().toUTCString()
  },
  methods: {
    handle_answered_image: function (result) {
      this.answers[this.images[this.current_img]._id] = result
      if (this.current_img === this.images.length - 1) {
        this.submit_results()
        this.done = true
      } else {
        this.current_img++
      }
    },
    handle_answered_meta: function (result) {
      this.answers[this.meta[this.current_meta].tag] = result
      if (this.current_meta === this.meta.length - 1) {
        this.metaDone = true
      } else {
        this.current_meta++
      }
    },
    submit_results: function () {
      this.timeend = new Date().toUTCString()
      this.answers['time'] = { start: this.timestart, end: this.timeend }
      this.answers['ticket'] = this.ticket
      fetch('/api/submit', { method: 'POST', body: JSON.stringify(this.answers) }).then(res => res.json()).then(json => { this.correct = json['correct']; this.total = json['total']; this.results = json['results'] })
    }
  }
}
</script>
<style>
progress{
  appearance: none;
  position: absolute;
  top: 0;
  left: 0;
  height: 5px;
  width: 100vw;
  color: transparent;
  background: none;
}

progress::-webkit-progress-value{
  background-color: firebrick;
}

</style>
