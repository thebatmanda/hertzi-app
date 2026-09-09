<script setup>
// Every view is its own fixed 390x844 "phone screen" component, so the app
// looks the same in the browser as it did as a design mockup. Swap this
// wrapper's max-width/centering for a fluid layout if you outgrow that.
</script>

<template>
  <div class="app-shell">
    <router-view />
  </div>
</template>

<style>
.app-shell {
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 24px 0;
  background: var(--hz-bg-warm);
}
</style>
