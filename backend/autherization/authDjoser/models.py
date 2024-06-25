from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionManager
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractUser, PermissionManager):
    email=models.EmailField(unique=True)
    firstName=models.CharField(max_length=255)
    lastName=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    objects=UserAccountManager()

    def get_full_name(self) -> str:
        return f"{self.firstName} {self.lastName}"
    
    def get_short_name(self) -> str:
        return self.firstName
    def __str__(self):
        return self.email