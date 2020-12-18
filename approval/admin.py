from django.contrib import admin
from .models import paper, related_person


admin.site.register(paper)
admin.site.register(related_person)