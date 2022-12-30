# Generated by Django 4.1.4 on 2022-12-30 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_dog', '0003_remove_photo_category_remove_rating_score_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_category', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('day_photo', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='my_dog.category')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(blank=True, max_length=256, null=True)),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='my_dog.photo')),
            ],
        ),
    ]
