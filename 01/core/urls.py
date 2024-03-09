from django.contrib import admin
from django.urls import path, include
from .views import home, salvar

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('', home, name='home'),
    path ('salvar/', salvar, name='salvar'),

]
