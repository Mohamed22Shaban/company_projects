from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Comment
# # from import_export.admin import ImportExportModelAdmin
# # from admin import ImportExportModelAdmin

admin.site.register(Post)
# @admin.register(Post)
# class PostImportExport(ImportExportModelAdmin):
#     pass


# admin.site.register(Comment)
# @admin.register(Comment)
# class CommentImportExport(ImportExportModelAdmin):
#     pass
# admin.site.register(Post, Comment)
