<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getProfile, getMe, getCompatibility } from '../services/api.js'

const props = defineProps({ id: [String, Number] })
const route = useRoute()
const router = useRouter()

const match = ref(null)
const score = ref(route.query.score ? Number(route.query.score) : null)
const loading = ref(true)
const scoreUnavailable = ref(false)

onMounted(async () => {
  try {
    match.value = await getProfile(props.id)
    if (score.value === null) {
      const me = await getMe()
      try {
        const result = await getCompatibility(me.id, props.id)
        score.value = result.score
      } catch {
        // The AI model needs `pip install sentence-transformers` to have
        // finished downloading its weights before it can score anything.
        scoreUnavailable.value = true
      }
    }
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="screen">
    <div class="glow"></div>

    <template v-if="!loading && match">
      <div class="portraits">
        <div class="portrait portrait--a">
          <svg width="34" height="34" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="8" r="3.8" stroke="#FFFFFF" stroke-width="1.6" />
            <path d="M5 20c0-3.9 3.1-6.2 7-6.2s7 2.3 7 6.2" stroke="#FFFFFF" stroke-width="1.6" stroke-linecap="round" />
          </svg>
        </div>
        <svg width="70" height="40" viewBox="0 0 70 40" class="connector">
          <path
            d="M0 20 Q 12 4, 23 20 T 46 20 T 70 20"
            stroke="var(--hz-pink)"
            stroke-width="2.5"
            fill="none"
            stroke-dasharray="3 5"
            stroke-linecap="round"
          />
        </svg>
        <div class="portrait portrait--b">
          <svg width="34" height="34" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="8" r="3.8" stroke="#FFFFFF" stroke-width="1.6" />
            <path d="M5 20c0-3.9 3.1-6.2 7-6.2s7 2.3 7 6.2" stroke="#FFFFFF" stroke-width="1.6" stroke-linecap="round" />
          </svg>
        </div>
      </div>

      <h1 class="headline hz-gradient-text">You're in sync!</h1>
      <p class="subcopy">
        You and {{ match.name }} are vibing at the same frequency. Say hi before the moment passes.
      </p>

      <div v-if="score !== null" class="sync-pill">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
          <path d="M2 12h4l2-7 4 14 3-9 2 4h5" stroke="var(--hz-pink-deep)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        <span>{{ score }}% compatibility</span>
      </div>
      <p v-else-if="scoreUnavailable" class="score-hint">
        Compatibility score not available yet — run <code>pip install -r requirements.txt</code>
        in <code>backend/</code> so the AI model can load.
      </p>

      <div class="cta-stack">
        <button class="cta" @click="router.push('/chat')">Send a message</button>
        <button class="ghost" @click="router.push('/discover')">Keep exploring</button>
      </div>
    </template>

    <p v-else-if="!loading" class="status">Couldn't load that match.</p>
  </div>
</template>

<style scoped>
.screen {
  position: relative;
  width: 390px;
  height: 844px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.glow {
  position: absolute;
  top: -70px;
  left: 50%;
  transform: translateX(-50%);
  width: 300px;
  height: 300px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(236, 72, 153, 0.14) 0%, rgba(236, 72, 153, 0) 70%);
}
.portraits {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 28px;
}
.portrait {
  width: 96px;
  height: 96px;
  border-radius: 50%;
  border: 4px solid #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
}
.portrait--a {
  background: linear-gradient(135deg, var(--hz-orange-light), var(--hz-orange));
  box-shadow: 0 10px 24px rgba(249, 115, 22, 0.25);
}
.portrait--b {
  background: linear-gradient(135deg, var(--hz-pink), var(--hz-purple-deep));
  box-shadow: 0 10px 24px rgba(236, 72, 153, 0.25);
}
.connector {
  margin: 0 -6px;
  z-index: 1;
}
.headline {
  position: relative;
  font-family: var(--font-display);
  font-size: 32px;
  font-weight: 700;
  text-align: center;
  margin: 0;
}
.subcopy {
  position: relative;
  font-size: 14px;
  color: var(--hz-ink-soft);
  text-align: center;
  line-height: 1.5;
  max-width: 280px;
  margin-top: 14px;
}
.sync-pill {
  position: relative;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 22px;
  background: var(--hz-chip-bg);
  padding: 9px 16px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 800;
  color: var(--hz-pink-deep);
}
.score-hint {
  position: relative;
  margin-top: 22px;
  font-size: 12px;
  color: var(--hz-ink-soft);
  text-align: center;
  max-width: 280px;
  line-height: 1.5;
}
.cta-stack {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  margin-top: 40px;
  width: 100%;
  padding: 0 40px;
}
.cta,
.ghost {
  width: 100%;
  height: 56px;
  border-radius: 28px;
  font-size: 15px;
  font-weight: 700;
  font-family: var(--font-body);
  cursor: pointer;
}
.cta {
  border: none;
  background: var(--hz-gradient);
  color: #ffffff;
  box-shadow: 0 12px 24px rgba(236, 72, 153, 0.28);
}
.ghost {
  border: 1.5px solid var(--hz-line);
  background: transparent;
  color: var(--hz-ink);
}
.status {
  color: var(--hz-ink-soft);
  font-size: 14px;
}
</style>
