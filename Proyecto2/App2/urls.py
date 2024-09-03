from django.urls import path
from . import views

urlpatterns = [
    path('Pagina 1/', views.pagina1),
    path('Pagina 2/', views.pagina2),
]