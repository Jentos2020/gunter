from django.views.generic import TemplateView
from .models import Photo
from random import randint


class MainPage(TemplateView):
    template_name = 'my_dog/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        max_pk = Photo.objects.latest('pk').pk
        photo = Photo.objects.filter(pk=randint(1, max_pk)).first()
        while not photo: photo = Photo.objects.filter(pk=randint(1, max_pk)).first()
        data['photo_name'] = photo
        print(photo)
        return data

class BioPage(TemplateView):
    template_name = 'my_dog/bio.html'

class APIPage(TemplateView):
    template_name = 'my_dog/api.html'