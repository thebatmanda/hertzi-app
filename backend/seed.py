"""
Populate the database with demo profiles so the app has something to show.

Run once with:  python seed.py
Safe to re-run: it clears and re-inserts the demo rows each time.
"""
from database import _connect, init_db

PROFILES = [
    dict(
        name="Alex Rivera",
        age=29,
        location="Denver, CO",
        bio=(
            "Coffee before 9am, vinyl after 9pm. Looking for someone who can "
            "hang during a long hike and a longer conversation."
        ),
        photo_url=None,
        is_me=1,
        interests=["Vinyl", "Hiking", "Cooking", "Live music", "Coffee"],
    ),
    dict(
        name="Maya",
        age=27,
        location="2 miles away",
        bio=(
            "Slow mornings, loud concerts. Currently rebuilding a record "
            "player I found at a flea market and looking for someone to "
            "break it in with."
        ),
        photo_url=None,
        is_me=0,
        interests=["Live music", "Vinyl", "Coffee"],
    ),
    dict(
        name="Jordan",
        age=31,
        location="5 miles away",
        bio=(
            "Trail runner on weekends, spreadsheet enthusiast on weekdays. "
            "Always up for a new coffee shop or a bad pun."
        ),
        photo_url=None,
        is_me=0,
        interests=["Hiking", "Coffee", "Running"],
    ),
    dict(
        name="Sam",
        age=26,
        location="8 miles away",
        bio=(
            "I cook too much food for one person on purpose, hoping someone "
            "will eventually help me eat it. Also: very serious about live "
            "music."
        ),
        photo_url=None,
        is_me=0,
        interests=["Cooking", "Live music"],
    ),
]


def seed() -> None:
    init_db()
    with _connect() as conn:
        conn.execute("DELETE FROM interests")
        conn.execute("DELETE FROM matches")
        conn.execute("DELETE FROM profiles")

        for profile in PROFILES:
            cursor = conn.execute(
                """INSERT INTO profiles (name, age, location, bio, photo_url, is_me)
                   VALUES (:name, :age, :location, :bio, :photo_url, :is_me)""",
                profile,
            )
            profile_id = cursor.lastrowid
            for label in profile["interests"]:
                conn.execute(
                    "INSERT INTO interests (profile_id, label) VALUES (?, ?)",
                    (profile_id, label),
                )
    print(f"Seeded {len(PROFILES)} profiles.")


if __name__ == "__main__":
    seed()
