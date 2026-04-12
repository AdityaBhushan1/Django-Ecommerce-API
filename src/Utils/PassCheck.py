import re
from rest_framework import serializers


def validate_password_strength(password: str):
    errors = []

    if len(password) < 8:
        errors.append(f"Must be at least 8 characters")

    if not re.search(r"[A-Z]", password):
        errors.append("Must contain at least one uppercase letter")

    if not re.search(r"[a-z]", password):
        errors.append("Must contain at least one lowercase letter")

    if not re.search(r"[0-9]", password):
        errors.append("Must contain at least one number")

    if not re.search(
        r"[!@#$%^&*(),.?\":{}|<>]", password
    ):
        errors.append("Must contain at least one special character")

    if errors:
        raise serializers.ValidationError({"password": errors})
