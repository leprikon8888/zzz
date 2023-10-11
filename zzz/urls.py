
from django.contrib import admin
from django.urls import path
from baza import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
]


