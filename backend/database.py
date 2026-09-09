"""
SQLite connection + schema bootstrap for Hertzi.

Uses Python's built-in `sqlite3` — no extra DB driver to install. Swap this
module for SQLAlchemy + Postgres later without touching the routers, as long
as you keep the same function signatures (get_db / init_db).
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "hertzi.db"
SCHEMA_PATH = Path(__file__).parent / "db" / "schema.sql"


def _connect() -> sqlite3.Connection:
    # check_same_thread=False: FastAPI runs sync dependencies and route
    # handlers in a thread pool, and a single request's "yield the
    # connection, close it after" span can hop threads between the two.
    # Each request still gets its own connection and uses it sequentially,
    # so this is safe here — it just stops sqlite3 from being overly strict
    # about which OS thread touches the object.
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Create tables if they don't exist yet. Safe to call on every boot."""
    with _connect() as conn:
        conn.executescript(SCHEMA_PATH.read_text())


def get_db():
    """FastAPI dependency: yields a connection, closes it after the request.

    FastAPI recognizes the `yield` and runs the code after it as teardown,
    so this plain generator function is used directly as `Depends(get_db)`.
    """
    conn = _connect()
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()
