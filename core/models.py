import uuid
from django.db import models
from django.contrib.auth.models import (
            AbstractBaseUser,
            PermissionsMixin,
            BaseUserManager
        )


class UserManager(BaseUserManager):
    # Manager for users

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('User must have an email address')

        # Email normalize
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # password hash
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):

        user = self.create_user(email, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # User in the system

    id = models.UUIDField(
            default=uuid.uuid4,
            editable=False,
            unique=True,
            primary_key=True
        )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'User'


class Category(models.Model):
    id = models.UUIDField(
            default=uuid.uuid4,
            editable=False,
            unique=True,
            primary_key=True
        )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)

    class Meta:
        db_table = 'Category'


class Tag(models.Model):
    id = models.UUIDField(
            default=uuid.uuid4,
            editable=False,
            unique=True,
            primary_key=True
        )
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Tag'