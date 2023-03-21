from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from mysite.models import Details,Projects
from .models import User
# Register your models here.
admin.site.register(Details)
admin.site.register(User,UserAdmin)
admin.site.register(Projects)
