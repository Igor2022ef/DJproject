from django.db import models
from django.urls import reverse


class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name='Рисунок графика')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

class Build_graf(models.Model):
    name_product = models.CharField(max_length=150, blank=True)
    cost = models.IntegerField(max_length=150, null=True)
    weight = models.CharField(max_length=150, blank=True)
    date = models.CharField(max_length=150, blank=True)
    shop = models.TextField(blank=True)

    def __str__(self):
        return self.name_product

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('category', kwargs={'cat_id': self.pk})
        return reverse('category', kwargs={'cat_slug': self.slug})
#
#
# class Graf(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Заголовок')
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
#     year = models.DateField(max_length=4)
#     index = models.DecimalField(blank=True,max_digits=32, decimal_places=2)
#     index_name = models.CharField(max_length=255)
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
#     time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
#     cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
#     articles = models.ForeignKey('Articles', on_delete=models.PROTECT, verbose_name='Статья')
#     is_published = models.BooleanField(default=True, verbose_name='Публикация')

