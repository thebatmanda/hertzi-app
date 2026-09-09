"""The AI-powered 'frequency compatibility' endpoint.

See ai/compatibility.py for how the score is actually computed (an
open-source Hugging Face sentence-embedding model, run locally).
"""
import sqlite3

from fastapi import APIRouter, Depends, HTTPException

from ai.compatibility import compatibility_score
from database import get_db
from models import CompatibilityRequest, CompatibilityResponse

router = APIRouter(prefix="/api/compatibility", tags=["compatibility"])


@router.post("", response_model=CompatibilityResponse)
def score_pair(req: CompatibilityRequest, conn: sqlite3.Connection = Depends(get_db)):
    profile_a = conn.execute(
        "SELECT bio FROM profiles WHERE id = ?", (req.profile_a_id,)
    ).fetchone()
    profile_b = conn.execute(
        "SELECT bio FROM profiles WHERE id = ?", (req.profile_b_id,)
    ).fetchone()
    if profile_a is None or profile_b is None:
        raise HTTPException(404, "One or both profile ids don't exist")

    try:
        score = compatibility_score(profile_a["bio"], profile_b["bio"])
    except ImportError as exc:
        raise HTTPException(
            503,
            "The AI compatibility model isn't installed yet — run "
            "`pip install -r requirements.txt` in backend/ (it pulls in "
            "sentence-transformers) and try again.",
        ) from exc
    return CompatibilityResponse(
        profile_a_id=req.profile_a_id,
        profile_b_id=req.profile_b_id,
        score=score,
    )
