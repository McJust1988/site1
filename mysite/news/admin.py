from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from. import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "create_at"]

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
#admin.site.register(models.Post)
#admin.site.register(models.News)
admin.site.register(models.Comment)
