<script setup>
// A starting point for real-time messaging — not wired to a backend yet.
import BottomTabBar from '../components/BottomTabBar.vue'
</script>

<template>
  <div class="screen">
    <header class="topbar">
      <span class="title">Chat</span>
    </header>
    <div class="empty">
      <p>No conversations yet.</p>
      <p class="hint">This is a good spot for a messages table + a websocket route.</p>
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
