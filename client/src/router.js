import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Survey from './views/Survey.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/survey',
      name: 'survey',
      component: Survey
    }
  ]
})
