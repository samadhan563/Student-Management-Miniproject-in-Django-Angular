from django.db import models

# Create your models here.
class User(models.Model):
    userName=models.CharField(max_length=30,unique=True,null=False)
    password=models.CharField(max_length=16,null=False)
    role=models.CharField(max_length=16,unique=False,null=False)

    def __str__(self) -> str:
        return self.userName

    def toString(self):
        return self.userName + self.password + self.role

class LoginRequest:
    userName:str='' 
    password:str=''
