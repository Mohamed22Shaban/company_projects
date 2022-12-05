from django.contrib import admin
from . import models
# Register your models here.
from .models import Post, Comment
# # from import_export.admin import ImportExportModelAdmin
# # from admin import ImportExportModelAdmin

# admin.site.register(Post)
# @admin.register(Post)
# class PostImportExport(ImportExportModelAdmin):
#     pass


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id','title','content', 'post_date','post_update','author']

# admin.site.register(Comment)
# @admin.register(Comment)
# class CommentImportExport(ImportExportModelAdmin):
#     pass
# admin.site.register(Post, Comment)
