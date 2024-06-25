from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionManager
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, firstName, lastName,is_admin=False, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        name=firstName+' '+lastName
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
    is_admin=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['firstName', 'lastName']

    objects=UserAccountManager()

    def get_full_name(self) -> str:
        return f"{self.firstName} {self.lastName}"
    
    def get_short_name(self) -> str:
        return self.firstName
    def __str__(self):
        return self.email