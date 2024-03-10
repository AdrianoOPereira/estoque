from django.contrib import admin
from django.urls import path, include
from .views import index, salvar, cadastro

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('index', index, name='index'),
    path ('salvar/', salvar, name='salvar'),
    path('cadastro', cadastro, name='cadastro'),
    

]
