from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'category', CategoriesAPI)
router.register(r'photo', PhotoAPI)

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('bio', BioPage.as_view(), name='bio'),
    path('api', APIPage.as_view(), name='api'),
    path('next_photo', next_photo, name='next_photo'),
    path('like_photo', like_photo, name='like_photo'),
    path('download_photo', download_photo, name='download_photo'),
    path('api/v1/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)