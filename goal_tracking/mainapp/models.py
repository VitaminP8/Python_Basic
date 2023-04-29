from django.db import models
from userapp.models import MyUser

# Create your models here.
class User (models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    surname = models.CharField(max_length=20, blank=False, null=False)
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Category (models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"


class Goal (models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=300, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    lateness = models.BooleanField(default=False)
    deadline = models.DateField(blank=False, null=False)
    started_at = models.DateField(auto_now_add=True)

    user = models.ForeignKey(MyUser, blank=True, null=True, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name}, is_active-{self.is_active}, started_at-{self.started_at}, user-{self.user}"

