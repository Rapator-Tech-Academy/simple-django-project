from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, User,
    UserManager, PermissionsMixin
)
from django.db.models.deletion import CASCADE


class UserManager(UserManager):
    def create_user(self, email, password=None):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class DateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserDevice(DateModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="device")
    device_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "User Device"
        verbose_name_plural = "User Devices"

    def __str__(self):
        return self.device_name


class UserLog(DateModel):
    CASES = (
        (1, ("Created")),
        (2, ("Updated")),
        (3, ("Deleted")),
    )
    user = models.CharField(max_length=100)
    case = models.PositiveIntegerField(choices=CASES)

    class Meta:
        verbose_name = "User log"
        verbose_name_plural = "User logs"

    def __str__(self):
        return f"{self.user} - {self.case}"