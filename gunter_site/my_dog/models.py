from django.db import models


class Category(models.Model):
    photo_category = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.photo_category


class Photo(models.Model):
    photo = models.ImageField()
    upload_date = models.DateTimeField(auto_now_add=True)
    day_photo = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.photo.name

class Rating(models.Model):
    score = models.ForeignKey(Photo, on_delete=models.PROTECT)
    like_date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=256, blank=True, null=True)
