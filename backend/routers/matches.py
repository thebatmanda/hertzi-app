"""Recording and listing matches."""
import sqlite3

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from database import get_db

router = APIRouter(prefix="/api/matches", tags=["matches"])


class NewMatch(BaseModel):
    profile_a_id: int
    profile_b_id: int
    compatibility_score: float | None = None


@router.get("")
def list_matches(conn: sqlite3.Connection = Depends(get_db)):
    rows = conn.execute(
        "SELECT * FROM matches ORDER BY matched_at DESC"
    ).fetchall()
    return [dict(r) for r in rows]


@router.post("", status_code=201)
def create_match(match: NewMatch, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.execute(
        """INSERT INTO matches (profile_a_id, profile_b_id, compatibility_score)
           VALUES (?, ?, ?)""",
        (match.profile_a_id, match.profile_b_id, match.compatibility_score),
    )
    return {"id": cursor.lastrowid, **match.model_dump()}
