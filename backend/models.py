"""Pydantic request/response schemas shared by the routers."""
from pydantic import BaseModel


class Interest(BaseModel):
    label: str


class Profile(BaseModel):
    id: int
    name: str
    age: int
    location: str | None = None
    bio: str
    photo_url: str | None = None
    is_me: bool = False
    interests: list[str] = []


class CompatibilityRequest(BaseModel):
    profile_a_id: int
    profile_b_id: int


class CompatibilityResponse(BaseModel):
    profile_a_id: int
    profile_b_id: int
    score: float
