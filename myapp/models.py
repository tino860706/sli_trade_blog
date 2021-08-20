from django.utils.text import slugify
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.urls import reverse
from django.db import models


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save()


class Category(models.Model):
    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return f'{self.title}'


class Vehicle(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    image = models.ImageField(default='', blank=True, upload_to='images')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(350, 200)],
                                     format='JPEG', options={'quality': 60})
    slug = models.SlugField(blank=True, default='')
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Vehicle, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])
