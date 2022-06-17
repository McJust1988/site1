from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from. import models


class PostAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "create_at", ]


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
