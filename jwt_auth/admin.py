from django.contrib import admin

from jwt_auth.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
