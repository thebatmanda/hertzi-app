# Hertzi

A starter codebase for the Hertzi app design: a Vue 3 frontend, a Python
(FastAPI) backend, a SQLite database, and an open-source AI model that scores
"compatibility" between two people's bios.

## Stack, and why

| Layer      | Choice                              | Language        |
| ---------- | ------------------------------------ | --------------- |
| Frontend   | Vue 3 (Vite, `<script setup>`)       | JavaScript + HTML/CSS |
| Backend    | FastAPI                              | Python 3.11+    |
| Database   | SQLite (Python's built-in `sqlite3`) | SQL             |
| AI         | `sentence-transformers` (Hugging Face, runs locally) | Python |

This matches what you asked for: Vue on the frontend, SQL for the database,
and an open-source AI library wired in and ready to use — Python has by far
the richest ecosystem of open-source AI/ML libraries (Hugging Face
`transformers`, `sentence-transformers`, PyTorch, scikit-learn, etc.), so the
backend is Python rather than Node, even though the original mockups were
just static HTML.

**What the AI actually does right now:** the `/api/compatibility` endpoint
embeds two profile bios with an open-source Hugging Face sentence-embedding
model (`all-MiniLM-L6-v2`) and returns a 0-100 "in sync" score from their
cosine similarity — no API key, no cloud calls, everything runs on your
machine. See `backend/ai/compatibility.py`. It's deliberately written as a
small, swappable module so you can drop in a different open-source model, or
a completely different AI feature, later.

## IDE

Use **VS Code** — it's free, and both halves of this stack are first-class
there:

- Install the **Vue - Official** extension (Vue.volar) for `.vue` file
  support, autocomplete, and type checking.
- Install the **Python** extension (Microsoft) for the backend — it gives you
  debugging, linting, and a virtual-environment picker.
- Optional but handy: an **SQLite Viewer** extension so you can browse
  `backend/hertzi.db` without leaving the editor.

(PyCharm or WebStorm work fine too if you already use JetBrains tools — VS
Code is just the one editor that handles both languages well without paying
for two separate IDEs.)

## Project layout

```
hertzi-app/
├── frontend/           Vue 3 + Vite app
│   └── src/
│       ├── views/       One component per screen (Onboarding, Discover, Match, Profile, ...)
│       ├── components/  Shared pieces (HzMark logo, bottom tab bar)
│       ├── styles/      tokens.css — every brand color/font in one place
│       ├── services/    api.js — talks to the backend
│       └── router/      Screen-to-URL mapping
└── backend/             FastAPI app
    ├── main.py           App entrypoint + CORS
    ├── database.py        SQLite connection
    ├── db/schema.sql       Table definitions
    ├── seed.py            Demo data (run once)
    ├── routers/           /api/profiles, /api/matches, /api/compatibility
    ├── ai/compatibility.py The open-source AI scoring model
    └── models.py           Request/response shapes
```

## Running it

You need two terminals — one for the backend, one for the frontend.

**Backend** (Python 3.11+):

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt   # first run downloads the AI model too — can take a few minutes
python seed.py                    # creates hertzi.db and adds demo profiles
uvicorn main:app --reload --port 8000
```

Leave that running. The API is now at http://localhost:8000, with
interactive docs at http://localhost:8000/docs.

**Frontend** (Node 18+), in a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the URL it prints (usually http://localhost:5173). Click through
Onboarding → Discover → like someone → see the AI-scored match → Profile.

If you skip the `pip install` step for the backend (or it's still
downloading the AI model), everything still works — the match screen just
shows a note that the compatibility score isn't ready yet instead of a
number.

## Where to go next

- Real photos: `profiles.photo_url` is already in the schema — point it at
  real image URLs or wire up file uploads.
- Real auth: right now "me" is just whichever profile has `is_me = 1` in the
  seed data. Swap that for real login before this goes further.
- Chat and the matches list (`frontend/src/views/ChatView.vue`,
  `MatchesListView.vue`) are intentionally left as simple starting points —
  the backend has no messages table yet.
- Swap SQLite for Postgres by replacing `backend/database.py` — the routers
  don't need to change if you keep the same function names.
