from rest_framework import serializers
from .models import *

'''
Первым реализован вариант с наследованием от встроенного класса ModelSerializer в котором 
все методы прописаны "из коробки"
'''

class Articlesserializer(serializers.ModelSerializer):
    class Meta:
            model = Articles
            fields = ('title', 'cat', 'content', 'time_create', 'time_update', 'is_published', 'slug')


'''
Ниже более сложный вариант, т.е. создание сериализатора вручную, самому
'''
# class Articlesserializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     slug = serializers.SlugField()
#     # photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name='Рисунок графика')
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     cat_id = serializers.IntegerField()
#     is_published = models.BooleanField(default=True)
#
#
#     def create(self, validated_data):
#         return Articles.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.time_create = validated_data.get('time_create', instance.time_create)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.save()
#         return instance





