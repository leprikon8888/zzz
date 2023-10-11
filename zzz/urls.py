from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from baza import views
from zzz import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
