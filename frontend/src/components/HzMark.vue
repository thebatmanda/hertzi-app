<script setup>
// The "Hz" logomark with its signature squiggle tail.
// variant "bold"  -> filled gradient tile (app icon / primary lockups)
// variant "text"  -> plain gradient text, no tile (compact headers)
defineProps({
  variant: { type: String, default: 'bold' }, // 'bold' | 'text'
  size: { type: Number, default: 40 },
})
</script>

<template>
  <div
    v-if="variant === 'bold'"
    class="hz-mark hz-mark--bold"
    :style="{ width: size + 'px', height: size + 'px', borderRadius: size * 0.24 + 'px' }"
  >
    <span :style="{ fontSize: size * 0.34 + 'px' }">Hz</span>
    <svg :width="size * 0.28" :height="size * 0.13" viewBox="0 0 46 20" class="squiggle">
      <path
        d="M2 14 Q 8 4, 14 14 T 26 14 T 38 14"
        stroke="#FFFFFF"
        stroke-width="3.5"
        fill="none"
        stroke-linecap="round"
      />
    </svg>
  </div>

  <div v-else class="hz-mark hz-mark--text" :style="{ fontSize: size + 'px' }">
    <span class="hz-gradient-text">Hz</span>
    <svg :width="size * 0.28" :height="size * 0.13" viewBox="0 0 46 20" class="squiggle">
      <path
        d="M2 14 Q 8 4, 14 14 T 26 14 T 38 14"
        stroke="var(--hz-pink)"
        stroke-width="3.5"
        fill="none"
        stroke-linecap="round"
      />
    </svg>
  </div>
</template>

<style scoped>
.hz-mark {
  display: inline-flex;
  align-items: center;
  font-family: var(--font-display);
  font-weight: 700;
  line-height: 1;
}
.hz-mark--bold {
  background: var(--hz-gradient-bold);
  color: #ffffff;
  justify-content: center;
  gap: 2px;
  flex-shrink: 0;
}
.hz-mark--text {
  gap: 2px;
}
.squiggle {
  margin-left: -2px;
  overflow: visible;
}
</style>
