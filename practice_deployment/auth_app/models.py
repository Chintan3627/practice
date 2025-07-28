from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


# Create your models here.



class CustomerUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomerUser(AbstractUser):
    username = None  # remove default username
    email = models.EmailField(unique=True)  # must be unique for login

    phone_number = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # ✅ DO NOT put 'email' here

    objects = CustomerUserManager()  # use custom manager

    class Meta:
        db_table = 'customer_user'  # ✅ correct attribute

    def __str__(self):
        return self.email

