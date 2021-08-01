from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class User(models.Model):
    userName = models.CharField(max_length=30, unique=True, null=False)
    password = models.CharField(max_length=16, null=False)
    role = models.CharField(max_length=16, unique=False, null=False)

    def __str__(self) -> str:
        return self.userName

    def toString(self):
        return self.userName + self.password + self.role


class UserProfile(models.Model):
    firstName = models.CharField(max_length=30, unique=True, null=False)
    lastName = models.CharField(max_length=16, null=False)
    emaiId = models.CharField(max_length=30, unique=True, null=False,default=None)
    mobileNumber = models.CharField(max_length=30, unique=True,default=None)
    dateOfBirth = models.DateField(unique=True,default=None)
    image = models.CharField(max_length=200, unique=False, null=False,default=None)
    user=models.OneToOneField(User,on_delete=CASCADE,default=None)

    def __str__(self) -> str:
        return self.firstName

    def toString(self):
        return self.firstName + self.lastName + self.emaiId + self.mobileNumber


class LoginRequest:
    userName: str = ''
    password: str = ''
