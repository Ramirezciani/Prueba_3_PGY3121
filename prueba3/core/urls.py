from django.urls import path 
from .views import index,nosotros, tienda, contacto, donaciones

urlpatterns = [
    path('', index,name="index"),
    path('', nosotros,name="nosotros"),
    path('', tienda,name="tienda"),
    path('', contacto,name="contacto"),
    path('', donaciones,name="donaciones"),

]