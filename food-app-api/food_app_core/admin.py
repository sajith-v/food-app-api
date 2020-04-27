from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from food_app_core import models
# Register your models here.


admin.site.register(models.User) 