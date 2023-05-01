from django.contrib import admin
from mainapp.models import User, Category, Goal

# Register your models here.
admin.site.register(Category)
admin.site.register(Goal)
