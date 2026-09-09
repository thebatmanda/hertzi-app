<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import HzMark from '../components/HzMark.vue'
import BottomTabBar from '../components/BottomTabBar.vue'
import { getProfiles, getMe, getCompatibility, createMatch } from '../services/api.js'

const router = useRouter()

const profiles = ref([])
const me = ref(null)
const index = ref(0)
const loading = ref(true)
const error = ref(null)

const current = computed(() => profiles.value[index.value] ?? null)

onMounted(async () => {
  try {
    const [profileList, myProfile] = await Promise.all([getProfiles(), getMe()])
    profiles.value = profileList
    me.value = myProfile
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
})

function pass() {
  if (index.value < profiles.value.length - 1) index.value += 1
}

async function like() {
  if (!current.value || !me.value) return
  try {
    const { score } = await getCompatibility(me.value.id, current.value.id)
    await createMatch(me.value.id, current.value.id, score)
    router.push({ name: 'match', params: { id: current.value.id }, query: { score } })
  } catch (e) {
    // The compatibility model needs `pip install sentence-transformers`
    // downloaded before it can score anything — fall back to just matching.
    router.push({ name: 'match', params: { id: current.value.id } })
  }
}
</script>

<template>
  <div class="screen">
    <header class="topbar">
      <div class="brand">
        <HzMark :size="34" variant="bold" />
        <span class="wordmark">hertzi</span>
      </div>
      <div class="icon-buttons">
        <button class="icon-btn" aria-label="Filters">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none">
            <path d="M4 6h16M7 12h10M10 18h4" stroke="var(--hz-pink-deep)" stroke-width="1.8" stroke-linecap="round" />
          </svg>
        </button>
        <button class="icon-btn" aria-label="Notifications">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
            <path
              d="M12 3a5 5 0 00-5 5v3.2c0 .6-.2 1.1-.6 1.6L5 15h14l-1.4-2.2c-.4-.5-.6-1-.6-1.6V8a5 5 0 00-5-5z"
              stroke="var(--hz-pink-deep)"
              stroke-width="1.7"
              stroke-linejoin="round"
            />
            <path d="M9.5 18a2.5 2.5 0 005 0" stroke="var(--hz-pink-deep)" stroke-width="1.7" stroke-linecap="round" />
          </svg>
        </button>
      </div>
    </header>

    <p v-if="loading" class="status">Loading profiles…</p>
    <p v-else-if="error" class="status status--error">
      Couldn't reach the API ({{ error }}). Is the backend running on port 8000?
    </p>
    <p v-else-if="!current" class="status">That's everyone nearby for now — check back later.</p>

    <div v-else class="card">
      <div class="card__photo">
        <svg width="120" height="120" viewBox="0 0 24 24" fill="none" opacity="0.35">
          <circle cx="12" cy="8" r="4" stroke="#FFFFFF" stroke-width="1.4" />
          <path d="M4 20c0-4.4 3.6-7 8-7s8 2.6 8 7" stroke="#FFFFFF" stroke-width="1.4" stroke-linecap="round" />
        </svg>
      </div>

      <div class="card__sync">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
          <path
            d="M2 12h4l2-7 4 14 3-9 2 4h5"
            stroke="var(--hz-pink-deep)"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
        <span>Shared interests</span>
      </div>

      <div class="card__info">
        <div class="card__name">{{ current.name }}, {{ current.age }}</div>
        <div class="card__location">{{ current.location }}</div>
        <div class="card__tags">
          <span v-for="tag in current.interests" :key="tag">{{ tag }}</span>
        </div>
      </div>
    </div>

    <div v-if="current" class="actions">
      <button class="action-btn action-btn--pass" aria-label="Pass" @click="pass">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
          <path d="M5 5l14 14M19 5L5 19" stroke="var(--hz-ink)" stroke-width="2" stroke-linecap="round" />
        </svg>
      </button>
      <button class="action-btn action-btn--like" aria-label="Like" @click="like">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
          <path
            d="M12 20.5s-8-5.2-8-11.2C4 5.9 6.2 4 8.7 4c1.6 0 3 .8 3.9 2.1C13.5 4.8 14.9 4 16.5 4 19 4 21.2 5.9 21.2 9.3 21.2 15.3 12 20.5 12 20.5z"
            fill="#FFFFFF"
          />
        </svg>
      </button>
      <button class="action-btn action-btn--boost" aria-label="Boost">
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none">
          <path d="M13 2 4 14h6l-1 8 9-12h-6l1-8z" stroke="var(--hz-pink-deep)" stroke-width="1.8" stroke-linejoin="round" />
        </svg>
      </button>
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
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 22px 20px 14px;
}
.brand {
  display: flex;
  align-items: center;
  gap: 8px;
}
.wordmark {
  font-family: var(--font-display);
  font-size: 19px;
  font-weight: 700;
}
.icon-buttons {
  display: flex;
  align-items: center;
  gap: 10px;
}
.icon-btn {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: none;
  background: var(--hz-chip-bg);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.status {
  padding: 40px 24px;
  text-align: center;
  color: var(--hz-ink-soft);
  font-size: 14px;
}
.status--error {
  color: var(--hz-pink-deep);
}
.card {
  flex: 1;
  margin: 6px 20px 0;
  border-radius: 28px;
  background: var(--hz-gradient-bold);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.card__photo {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}
.card__sync {
  position: absolute;
  top: 18px;
  right: 18px;
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.92);
  padding: 8px 14px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 800;
  color: var(--hz-pink-deep);
}
.card__info {
  padding: 24px 24px 28px;
  background: linear-gradient(0deg, rgba(0, 0, 0, 0.42) 0%, rgba(0, 0, 0, 0) 100%);
  color: #ffffff;
}
.card__name {
  font-size: 24px;
  font-weight: 800;
}
.card__location {
  font-size: 13px;
  margin-top: 4px;
  color: rgba(255, 255, 255, 0.9);
}
.card__tags {
  display: flex;
  gap: 8px;
  margin-top: 14px;
  flex-wrap: wrap;
}
.card__tags span {
  background: rgba(255, 255, 255, 0.22);
  font-size: 11px;
  font-weight: 700;
  padding: 6px 12px;
  border-radius: 14px;
}
.actions {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 22px;
  padding: 22px 20px;
}
.action-btn {
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}
.action-btn--pass,
.action-btn--boost {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: #ffffff;
  border: 1.5px solid var(--hz-line);
  box-shadow: 0 6px 14px rgba(32, 18, 51, 0.06);
}
.action-btn--like {
  width: 68px;
  height: 68px;
  border-radius: 50%;
  background: var(--hz-gradient);
  box-shadow: 0 14px 24px rgba(236, 72, 153, 0.35);
}
</style>
