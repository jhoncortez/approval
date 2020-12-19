from django.contrib import admin
from .models import Mbr, PER_list, Mbr_PER_list

# Register your models here.

admin.site.register(Mbr)
admin.site.register(PER_list)
admin.site.register(Mbr_PER_list)