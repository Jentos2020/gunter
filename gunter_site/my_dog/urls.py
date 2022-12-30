from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('bio', BioPage.as_view(), name='bio'),
    path('api', APIPage.as_view(), name='api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)