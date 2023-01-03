from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from .models import Photo, Rating, Category
from random import randint
from django.views.decorators.csrf import csrf_exempt

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
