"""Tests for type definitions and Pydantic models."""

import pytest
from zopassport.types import ZoUser, ZoAuthResponse, ZoProfileResponse

class TestTypes:
    """Tests for Pydantic models."""

    def test_zo_user_validation(self):
        """Test ZoUser model validation."""
        user_data = {
            "id": "123",
            "first_name": "Test",
            "email_address": "test@example.com"
        }
        user = ZoUser(**user_data)
        assert user.id == "123"
        assert user.first_name == "Test"
        assert user.last_name is None

    def test_zo_auth_response_validation(self):
        """Test ZoAuthResponse validation."""
        data = {
            "user": {"id": "123"},
            "access_token": "access",
            "refresh_token": "refresh",
            "access_token_expiry": "expiry",
            "refresh_token_expiry": "expiry"
        }
        response = ZoAuthResponse(**data)
        assert response.user.id == "123"
        assert response.access_token == "access"

    def test_zo_profile_response_validation(self):
        """Test ZoProfileResponse validation."""
        data = {
            "id": "123",
            "first_name": "Test",
            "bio": "Bio"
        }
        profile = ZoProfileResponse(**data)
        assert profile.id == "123"
        assert profile.bio == "Bio"
