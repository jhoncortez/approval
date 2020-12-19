from django.contrib import admin
from django.urls import path, include

# https://domain.com/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('approval/', include('approval.urls')),
]
