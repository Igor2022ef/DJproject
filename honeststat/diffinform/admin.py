from django.contrib import admin
from .models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ArticlesResource(resources.ModelResource):
    class Meta:
        model = Articles
        exclude = ('title', 'slug', 'content', 'photo', 'time_create', 'cat', 'time_update', 'is_published')
# вывод данных на странице
class ArticlesAdmin(ImportExportModelAdmin):
    resource_classes = [ArticlesResource]
    list_display = ('title', 'name', 'is_published')
    search_fields = ('title', 'name')
    # prepopulated_fields = {"slug": ("title",)}

admin.site.register(Articles, ArticlesAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)


