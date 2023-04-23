from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, password: str | None, **other):
        email = self.normalize_email(email)
        user = self.model(email=email, **other)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str, **other):
        other.setdefault('is_staff', True)
        other.setdefault('is_superuser', True)
        other.setdefault('is_active', True)

        if other.get('is_staff') is not True:
            raise ValueError('Superuser must have field is_staff equal to True.')
        if other.get('is_superuser') is not True:
            raise ValueError('Superuser must have field is_superuser equal to True.')

        return self.create_user(email, password, **other)