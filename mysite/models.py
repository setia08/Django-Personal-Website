from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=64)
    phone=models.IntegerField(max_length=20)
    email=models.CharField(max_length=64)
    description=models.TextField()

    def __str__(self):
        return f"{self.name}"
    

class Projects(models.Model):
    title=models.CharField(max_length=64)
    image=models.ImageField(upload_to="images/")
    git_link=models.CharField(max_length=100)
    project_description=models.CharField(max_length=200)

    def __str__(self):
        return f"Project name: {self.title}"