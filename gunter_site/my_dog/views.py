from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Photo, Rating, Category
from random import randint
from django.views.decorators.csrf import csrf_exempt

from .serializers import CategorySerializer, PhotoSerializer, AllPhotoSerializer

max_pk = None
photo = None
likes_count = 0


class MainPage(TemplateView):
    template_name = 'my_dog/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        global max_pk
        global photo
        global likes_count
        max_pk = Photo.objects.latest('pk').pk
        photo = Photo.objects.filter(pk=randint(1, max_pk)).first()
        while not photo: photo = Photo.objects.filter(pk=randint(1, max_pk)).first()
        data['photo_name'] = photo
        data['likes_count'] = likes_count = Rating.objects.filter(score=photo).count()
        data['categories'] = photo.category.all()
        return data


def download_photo(request):
    if request.method == 'GET':
        global photo
        current_photo = Photo.objects.get(pk=photo.pk)
        if current_photo.downloads:
            a = current_photo.downloads
            current_photo.downloads = a + 1
            current_photo.save()
        else:
            current_photo.downloads = 1
            current_photo.save()
        return HttpResponse(photo.photo.url)
    else:
        return HttpResponse("Only GET allowed")

def next_photo(request):
    if request.method == 'GET':
        global max_pk
        global photo
        global likes_count
        likes_count = Rating.objects.filter(score=photo).count()
        photo = Photo.objects.filter(pk=randint(1, max_pk)).first()
        while not photo: photo = Photo.objects.filter(pk=randint(1, max_pk)).first()
        return JsonResponse(
            data={
                'photo': photo.photo.url,
                'likes': likes_count,
                'cats': list(photo.category.all().values()),
            },
        )
    else:
        return HttpResponse("Only GET allowed")


@csrf_exempt
def like_photo(request):
    global likes_count
    if request.method == 'POST':
        likes_count += 1
        Rating.objects.create(score=photo).save()
        return JsonResponse(
            data={
                'likes': likes_count,
            },
        )
    else:
        return HttpResponse("Only POST allowed")


class BioPage(TemplateView):
    template_name = 'my_dog/bio.html'


class APIPage(TemplateView):
    template_name = 'my_dog/api.html'


class CategoriesAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def photo(self, request, pk=None):
        category = self.get_object()
        photo = Photo.objects.filter(category=category)
        serializer = PhotoSerializer(photo, many=True)
        return Response(serializer.data)


class PhotoAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = AllPhotoSerializer

    @action(detail=True, methods=['get'])
    def info(self, request, pk=None):
        photo_id = self.get_object()
        photo = Photo.objects.filter(pk=photo_id.pk)
        serializer = PhotoSerializer(photo, many=True)
        return Response({'data': serializer.data, 'likes': Rating.objects.filter(score=photo_id.pk).count()})
