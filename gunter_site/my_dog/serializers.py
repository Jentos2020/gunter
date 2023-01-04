from rest_framework import serializers
from .models import Photo, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        exclude = ['day_photo']


class AllPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo', 'pk', 'category']