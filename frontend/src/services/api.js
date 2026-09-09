// Thin wrapper around the FastAPI backend. Point VITE_API_URL at a different
// host (see .env.example) if the backend isn't running on localhost:8000.
const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

async function request(path, options) {
  const res = await fetch(`${BASE_URL}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })
  if (!res.ok) {
    throw new Error(`API error ${res.status}: ${await res.text()}`)
  }
  return res.json()
}

export function getProfiles() {
  return request('/profiles')
}

export function getProfile(id) {
  return request(`/profiles/${id}`)
}

export function getMe() {
  return request('/profiles/me')
}

export function getCompatibility(profileAId, profileBId) {
  return request('/compatibility', {
    method: 'POST',
    body: JSON.stringify({ profile_a_id: profileAId, profile_b_id: profileBId }),
  })
}

export function createMatch(profileAId, profileBId, compatibilityScore) {
  return request('/matches', {
    method: 'POST',
    body: JSON.stringify({
      profile_a_id: profileAId,
      profile_b_id: profileBId,
      compatibility_score: compatibilityScore,
    }),
  })
}
