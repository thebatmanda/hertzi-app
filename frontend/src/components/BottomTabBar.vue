<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()

const tabs = [
  { name: 'discover', label: 'Discover', to: '/discover' },
  { name: 'matches', label: 'Matches', to: '/matches' },
  { name: 'chat', label: 'Chat', to: '/chat' },
  { name: 'profile', label: 'Profile', to: '/profile' },
]
</script>

<template>
  <nav class="tab-bar">
    <router-link
      v-for="tab in tabs"
      :key="tab.name"
      :to="tab.to"
      class="tab"
      :class="{ 'tab--active': route.path.startsWith(tab.to) }"
    >
      <span class="tab-label hz-label">{{ tab.label }}</span>
    </router-link>
  </nav>
</template>

<style scoped>
.tab-bar {
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 14px 12px 22px;
  border-top: 1px solid var(--hz-line);
  background: var(--hz-bg);
}
.tab {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  min-width: 44px;
  min-height: 44px;
  justify-content: center;
}
.tab-label {
  font-size: 9px;
  font-weight: 700;
  color: var(--hz-muted);
}
.tab--active .tab-label {
  color: var(--hz-pink-deep);
}
</style>
