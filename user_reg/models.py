
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели E-Mail")
        if not username:
            raise ValueError("Вы не ввели Логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)
    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)

class Role(models.TextChoices):
    Admin = 'AD',_('Admin')
    User = 'US', _('User')

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    role = models.CharField(
        max_length=2,
        choices=Role.choices,
        default=Role.User,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return self.email