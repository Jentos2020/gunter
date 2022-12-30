from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('bio', BioPage.as_view(), name='bio'),
    path('api', APIPage.as_view(), name='api'),
]
