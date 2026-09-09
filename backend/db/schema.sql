-- Hertzi database schema (SQLite).
-- Run automatically by database.py on first start.

CREATE TABLE IF NOT EXISTS profiles (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    age         INTEGER NOT NULL,
    location    TEXT,
    bio         TEXT NOT NULL,
    photo_url   TEXT,
    is_me       INTEGER NOT NULL DEFAULT 0,   -- 1 for the signed-in demo user
    created_at  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS interests (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id  INTEGER NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    label       TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS matches (
    id                   INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_a_id         INTEGER NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    profile_b_id         INTEGER NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
    compatibility_score  REAL,
    matched_at           TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_interests_profile ON interests(profile_id);
CREATE INDEX IF NOT EXISTS idx_matches_profile_a ON matches(profile_a_id);
