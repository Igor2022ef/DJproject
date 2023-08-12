from django.contrib import admin
from .models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

# класс обработки данных
class Build_grafResource(resources.ModelResource):
    class Meta:
        model = Build_graf

# вывод данных на странице
class Build_grafAdmin(ImportExportModelAdmin):
    resource_classes = [Build_grafResource]
    list_display = ('name_product', 'shop')
    search_fields = ('name', 'shop')

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Build_graf, Build_grafAdmin)
