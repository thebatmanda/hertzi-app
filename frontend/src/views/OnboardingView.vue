<script setup>
import { useRouter } from 'vue-router'
import HzMark from '../components/HzMark.vue'

const router = useRouter()
</script>

<template>
  <div class="screen">
    <div class="blob blob--top-right"></div>
    <div class="blob blob--left"></div>

    <header class="brand">
      <HzMark :size="64" variant="bold" />
      <div class="wordmark hz-gradient-text">hertzi</div>
      <div class="tagline hz-label">Find your frequency.</div>
    </header>

    <div class="wave">
      <svg width="150" height="80" viewBox="0 0 150 80">
        <path
          d="M0 40 Q 12 12, 25 40 T 50 40 T 75 40 T 100 40 T 125 40 T 150 40"
          stroke="var(--hz-orange)"
          stroke-width="2.5"
          fill="none"
        />
        <path
          d="M0 40 Q 12 68, 25 40 T 50 40 T 75 40 T 100 40 T 125 40 T 150 40"
          stroke="var(--hz-pink)"
          stroke-width="2.5"
          fill="none"
          opacity="0.55"
        />
      </svg>
    </div>

    <div class="copy">
      <h1>Find people who vibrate at your frequency.</h1>
      <p>
        Answer a few honest questions and we'll match you with people who are
        actually in sync — not just nearby.
      </p>
    </div>

    <div class="actions">
      <button class="cta" @click="router.push('/discover')">Get Started</button>
      <p class="login-hint">Already have an account? <a href="#">Log in</a></p>
    </div>
  </div>
</template>

<style scoped>
.screen {
  position: relative;
  width: 390px;
  height: 844px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  margin: 0 auto;
}
.blob {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
}
.blob--top-right {
  top: -60px;
  right: -70px;
  width: 220px;
  height: 220px;
  background: radial-gradient(
    circle,
    rgba(249, 115, 22, 0.16) 0%,
    rgba(236, 72, 153, 0.12) 55%,
    rgba(236, 72, 153, 0) 75%
  );
}
.blob--left {
  top: 120px;
  left: -90px;
  width: 180px;
  height: 180px;
  background: radial-gradient(circle, rgba(236, 72, 153, 0.1) 0%, rgba(236, 72, 153, 0) 70%);
}
.brand {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 72px 32px 40px;
  gap: 14px;
}
.wordmark {
  font-family: var(--font-display);
  font-size: 30px;
  font-weight: 700;
}
.tagline {
  font-size: 11px;
  font-weight: 700;
  color: var(--hz-pink-deep);
}
.wave {
  position: relative;
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0.85;
}
.copy {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  padding: 0 32px;
  text-align: center;
}
.copy h1 {
  font-size: 26px;
  font-weight: 800;
  line-height: 1.25;
  margin: 0;
}
.copy p {
  font-size: 14px;
  color: var(--hz-ink-soft);
  line-height: 1.5;
  margin: 0;
}
.actions {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  padding: 36px 32px 44px;
}
.cta {
  width: 100%;
  height: 56px;
  border: none;
  border-radius: 28px;
  background: var(--hz-gradient);
  color: #ffffff;
  font-size: 16px;
  font-weight: 700;
  font-family: var(--font-body);
  cursor: pointer;
  box-shadow: 0 12px 24px rgba(236, 72, 153, 0.28);
}
.login-hint {
  font-size: 13px;
  color: var(--hz-ink-soft);
  margin: 0;
}
</style>
