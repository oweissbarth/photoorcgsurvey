<template>
<div class="survey">
<single-choice-question v-if="!metaDone && !done" :question="meta[current_meta].question" :answers="meta[current_meta].answers" @answered="handle_answered_meta"/>
<image-question v-if="metaDone && !done" :imagehash="images[current_img]" @answered="handle_answered_image"/>
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
        { tag: '3d-software', question: 'How often do you use 3D-Software (Blender, UE4, Modo, ZBrush, etc...)?', answers: ['Never', 'Once a month', 'Once a week', 'Multiple times a week', 'Everyday'] },
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
      results: []
    }
  },
  mounted () {
    fetch('/api/').then(res => res.json()).then(res => { this.images = res })
  },
  methods: {
    handle_answered_image: function (result) {
      this.answers[this.images[this.current_img]] = result
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
      fetch('/api/submit', { method: 'POST', body: JSON.stringify(this.answers) }).then(res => res.json()).then(json => { this.correct = json['correct']; this.total = json['total']; this.results = json['results'] })
    }
  }
}
</script>
