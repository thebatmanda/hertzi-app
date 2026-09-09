"""
"Frequency compatibility" scoring, powered by an open-source sentence-embedding
model from Hugging Face (sentence-transformers). Everything runs locally on
your machine (CPU is fine) — no API key, no network calls, no cloud bill.

How it works: each bio is embedded into a vector that captures its meaning,
then we compare the two vectors with cosine similarity. Two bios about "vinyl,
hiking and slow mornings" end up numerically close; wildly different bios end
up far apart. That similarity gets mapped onto a friendlier 0-100 "in sync %".

Swap-friendly by design: change MODEL_NAME to any other embedding model on
the Hugging Face Hub (e.g. a bigger, more accurate one) without touching the
routers that call `compatibility_score()`.
"""
from functools import lru_cache

import numpy as np

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def _get_model():
    # Imported lazily so the API server can boot (and every other route can
    # work) even before `pip install sentence-transformers` has finished, and
    # so the ~90MB model only downloads the first time it's actually needed.
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(MODEL_NAME)


def compatibility_score(bio_a: str, bio_b: str) -> float:
    """Return a 0-100 'in sync' percentage for two profile bios."""
    model = _get_model()
    embedding_a, embedding_b = model.encode([bio_a, bio_b])

    cosine_similarity = float(
        np.dot(embedding_a, embedding_b)
        / (np.linalg.norm(embedding_a) * np.linalg.norm(embedding_b))
    )
    # cosine similarity is -1..1 — rescale to a 0-100 percentage for the UI.
    in_sync_percent = (cosine_similarity + 1) / 2 * 100
    return round(in_sync_percent, 1)
