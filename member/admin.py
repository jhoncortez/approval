from django.contrib import admin
from .models import User, UserAuth, AuthInfo

# Register your models here.

admin.site.register(User)
admin.site.register(UserAuth)
admin.site.register(AuthInfo)