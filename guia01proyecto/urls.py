from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('inicio/', admin.site.urls),
    path('app01/', include("App01.urls")),
]
