<script setup>
// A starting point — wire this up to GET /api/matches (see services/api.js)
// once you're ready to list real matches instead of this placeholder.
import BottomTabBar from '../components/BottomTabBar.vue'
</script>

<template>
  <div class="screen">
    <header class="topbar">
      <span class="title">Matches</span>
    </header>
    <div class="empty">
      <p>Your matches will show up here.</p>
      <p class="hint">Wire this view up to <code>GET /api/matches</code>.</p>
    </div>
    <BottomTabBar />
  </div>
</template>

<style scoped>
.screen {
  width: 390px;
  height: 844px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.topbar {
  padding: 22px 20px 14px;
}
.title {
  font-family: var(--font-display);
  font-size: 22px;
  font-weight: 700;
}
.empty {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  text-align: center;
  padding: 0 32px;
  color: var(--hz-ink-soft);
  font-size: 14px;
}
.hint {
  font-size: 12px;
}
</style>
