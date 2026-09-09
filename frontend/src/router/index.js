import { createRouter, createWebHistory } from 'vue-router'

import OnboardingView from '../views/OnboardingView.vue'
import DiscoverView from '../views/DiscoverView.vue'
import MatchView from '../views/MatchView.vue'
import ProfileView from '../views/ProfileView.vue'
import MatchesListView from '../views/MatchesListView.vue'
import ChatView from '../views/ChatView.vue'

const routes = [
  { path: '/', name: 'onboarding', component: OnboardingView },
  { path: '/discover', name: 'discover', component: DiscoverView },
  { path: '/match/:id', name: 'match', component: MatchView, props: true },
  { path: '/matches', name: 'matches', component: MatchesListView },
  { path: '/chat', name: 'chat', component: ChatView },
  { path: '/profile', name: 'profile', component: ProfileView },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
