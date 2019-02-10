from django.conf import settings
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from example import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls , name='admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
