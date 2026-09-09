"""Profile endpoints: the discover deck, one profile, and "me"."""
import sqlite3

from fastapi import APIRouter, Depends, HTTPException

from database import get_db
from models import Profile

router = APIRouter(prefix="/api/profiles", tags=["profiles"])


def _row_to_profile(conn: sqlite3.Connection, row: sqlite3.Row) -> Profile:
    interests = conn.execute(
        "SELECT label FROM interests WHERE profile_id = ? ORDER BY id", (row["id"],)
    ).fetchall()
    return Profile(
        id=row["id"],
        name=row["name"],
        age=row["age"],
        location=row["location"],
        bio=row["bio"],
        photo_url=row["photo_url"],
        is_me=bool(row["is_me"]),
        interests=[r["label"] for r in interests],
    )


@router.get("", response_model=list[Profile])
def list_profiles(conn: sqlite3.Connection = Depends(get_db)):
    """The discover deck: everyone except the signed-in demo user."""
    rows = conn.execute(
        "SELECT * FROM profiles WHERE is_me = 0 ORDER BY id"
    ).fetchall()
    return [_row_to_profile(conn, r) for r in rows]


@router.get("/me", response_model=Profile)
def get_me(conn: sqlite3.Connection = Depends(get_db)):
    row = conn.execute("SELECT * FROM profiles WHERE is_me = 1 LIMIT 1").fetchone()
    if row is None:
        raise HTTPException(404, "No demo user found — did you run seed.py?")
    return _row_to_profile(conn, row)


@router.get("/{profile_id}", response_model=Profile)
def get_profile(profile_id: int, conn: sqlite3.Connection = Depends(get_db)):
    row = conn.execute(
        "SELECT * FROM profiles WHERE id = ?", (profile_id,)
    ).fetchone()
    if row is None:
        raise HTTPException(404, f"No profile with id {profile_id}")
    return _row_to_profile(conn, row)
