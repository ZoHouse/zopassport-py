from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class ZoAvatar(BaseModel):
    """User avatar information."""

    status: str
    image: Optional[str] = None


class ZoUser(BaseModel):
    """Zo World user profile."""

    id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    bio: Optional[str] = None
    date_of_birth: Optional[str] = None
    place_name: Optional[str] = None
    body_type: Optional[str] = None
    pfp_image: Optional[str] = None
    email_address: Optional[str] = None
    mobile_country_code: Optional[str] = None
    mobile_number: Optional[str] = None
    wallet_address: Optional[str] = None
    membership: Optional[str] = None
    cultures: Optional[List[str]] = None
    avatar: Optional[ZoAvatar] = None
    role: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class ZoProfileResponse(BaseModel):
    """User profile API response."""

    id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    bio: Optional[str] = None
    date_of_birth: Optional[str] = None
    location: Optional[Dict[str, Any]] = None
    body_type: Optional[str] = None
    pfp_image: Optional[str] = None
    email_address: Optional[str] = None
    mobile_country_code: Optional[str] = None
    mobile_number: Optional[str] = None
    wallet_address: Optional[str] = None
    zo_membership: Optional[str] = None
    cultures: Optional[List[str]] = None
    avatar: Optional[ZoAvatar] = None
    founder_nfts: Optional[List[Any]] = None
    founder_nfts_count: Optional[int] = None
    role: Optional[str] = None


class ZoAuthResponse(BaseModel):
    """Authentication API response."""

    user: ZoUser
    access_token: str
    refresh_token: str
    access_token_expiry: str
    refresh_token_expiry: str
    device_id: Optional[str] = None
    device_secret: Optional[str] = None


class ZoTokenRefreshResponse(BaseModel):
    """Token refresh API response."""

    access: str
    refresh: str
    access_expiry: str
    refresh_expiry: str


class ZoErrorResponse(BaseModel):
    """Standard API error response."""

    success: Optional[bool] = False
    error: Optional[str] = None
    message: Optional[str] = None
    detail: Optional[str] = None
    errors: Optional[List[str]] = None


class ZoAvatarGenerateResponse(BaseModel):
    """Avatar generation initiation response."""

    task_id: str
    status: str


class ZoAvatarStatusResponse(BaseModel):
    """Avatar generation status response."""

    task_id: str
    status: str
    result: Optional[Dict[str, Any]] = None
