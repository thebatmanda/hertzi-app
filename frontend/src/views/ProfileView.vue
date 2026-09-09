<script setup>
import { ref, onMounted } from 'vue'
import BottomTabBar from '../components/BottomTabBar.vue'
import { getMe } from '../services/api.js'

const me = ref(null)
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    me.value = await getMe()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="screen">
    <p v-if="loading" class="status">Loading profile…</p>
    <p v-else-if="error" class="status status--error">Couldn't reach the API ({{ error }}).</p>

    <template v-else-if="me">
      <div class="header">
        <button class="edit-btn" aria-label="Edit cover photo">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
            <path d="M4 20l1-5 11-11 4 4-11 11-5 1z" stroke="#FFFFFF" stroke-width="1.7" stroke-linejoin="round" />
          </svg>
        </button>
        <div class="avatar">
          <svg width="38" height="38" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="8" r="3.8" stroke="var(--hz-orange)" stroke-width="1.6" />
            <path d="M5 20c0-3.9 3.1-6.2 7-6.2s7 2.3 7 6.2" stroke="var(--hz-orange)" stroke-width="1.6" stroke-linecap="round" />
          </svg>
        </div>
      </div>

      <div class="identity">
        <div class="name">{{ me.name }}, {{ me.age }}</div>
        <div class="location">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none">
            <path d="M12 21s-7-5.4-7-11.4A7 7 0 0112 3a7 7 0 017 6.6C19 15.6 12 21 12 21z" stroke="var(--hz-ink-soft)" stroke-width="1.6" />
            <circle cx="12" cy="9.5" r="2.2" stroke="var(--hz-ink-soft)" stroke-width="1.6" />
          </svg>
          <span>{{ me.location }}</span>
        </div>
      </div>

      <div class="stats">
        <div class="stat">
          <div class="stat__value">128</div>
          <div class="stat__label hz-label">Matches</div>
        </div>
        <div class="stat">
          <div class="stat__value">91%</div>
          <div class="stat__label hz-label">Sync score</div>
        </div>
        <div class="stat">
          <div class="stat__value">14</div>
          <div class="stat__label hz-label">Day streak</div>
        </div>
      </div>

      <section class="section">
        <div class="section__title hz-label">About</div>
        <p class="bio">{{ me.bio }}</p>
      </section>

      <section class="section">
        <div class="section__title hz-label">Interests</div>
        <div class="chips">
          <span v-for="tag in me.interests" :key="tag">{{ tag }}</span>
        </div>
      </section>

      <section class="section">
        <div class="section__title hz-label">My frequency</div>
        <div class="frequency-bar">
          <svg width="100%" height="34" viewBox="0 0 334 34" preserveAspectRatio="none">
            <path
              d="M0 17 Q 20 3, 40 17 T 80 17 T 120 17 T 160 17 T 200 17 T 240 17 T 280 17 T 334 17"
              stroke="var(--hz-pink)"
              stroke-width="2"
              fill="none"
            />
          </svg>
          <div class="frequency-marker"></div>
        </div>
        <div class="frequency-scale">
          <span class="hz-label">Calm</span>
          <span class="hz-label">Energetic</span>
        </div>
      </section>

      <div class="spacer"></div>

      <div class="edit-profile">
        <button class="cta">Edit profile</button>
      </div>
    </template>

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
.status {
  padding: 40px 24px;
  text-align: center;
  color: var(--hz-ink-soft);
  font-size: 14px;
}
.status--error {
  color: var(--hz-pink-deep);
}
.header {
  position: relative;
  height: 150px;
  background: var(--hz-gradient-bold);
  flex-shrink: 0;
}
.edit-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: none;
  background: rgba(255, 255, 255, 0.28);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.avatar {
  position: absolute;
  left: 28px;
  bottom: -38px;
  width: 92px;
  height: 92px;
  border-radius: 50%;
  background: #fff4ec;
  border: 4px solid #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 18px rgba(32, 18, 51, 0.12);
}
.identity {
  padding: 52px 28px 0;
}
.name {
  font-size: 22px;
  font-weight: 800;
}
.location {
  display: flex;
  align-items: center;
  gap: 5px;
  margin-top: 6px;
  font-size: 13px;
  color: var(--hz-ink-soft);
}
.stats {
  display: flex;
  gap: 10px;
  padding: 22px 28px 0;
}
.stat {
  flex: 1;
  background: var(--hz-chip-bg);
  border-radius: 16px;
  padding: 14px 10px;
  text-align: center;
}
.stat__value {
  font-size: 18px;
  font-weight: 800;
  color: var(--hz-pink-deep);
}
.stat__label {
  font-size: 9px;
  font-weight: 700;
  color: var(--hz-ink-soft);
  margin-top: 4px;
}
.section {
  padding: 24px 28px 0;
}
.section__title {
  font-size: 11px;
  font-weight: 700;
  color: var(--hz-ink-soft);
  margin-bottom: 8px;
}
.bio {
  font-size: 13.5px;
  color: #3e3149;
  line-height: 1.55;
  margin: 0;
}
.chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.chips span {
  background: var(--hz-chip-bg);
  color: var(--hz-pink-deep);
  font-size: 12px;
  font-weight: 700;
  padding: 7px 13px;
  border-radius: 14px;
}
.frequency-bar {
  position: relative;
}
.frequency-marker {
  position: absolute;
  left: 62%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--hz-orange);
  border: 3px solid #ffffff;
  box-shadow: 0 3px 8px rgba(249, 115, 22, 0.4);
}
.frequency-scale {
  display: flex;
  justify-content: space-between;
  margin-top: 6px;
}
.frequency-scale span {
  font-size: 9px;
  font-weight: 700;
  color: var(--hz-muted);
}
.spacer {
  flex: 1;
}
.edit-profile {
  padding: 20px 28px 30px;
}
.cta {
  width: 100%;
  height: 52px;
  border: none;
  border-radius: 26px;
  background: var(--hz-gradient);
  color: #ffffff;
  font-size: 15px;
  font-weight: 700;
  font-family: var(--font-body);
  cursor: pointer;
  box-shadow: 0 10px 20px rgba(236, 72, 153, 0.25);
}
</style>
