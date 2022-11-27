from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Clients)
# admin.site.register(Project)
admin.site.register(EmailSender)
admin.site.register(EmailSubscribe)
admin.site.register(Project)
admin.site.register(Sales)
admin.site.register(RecievMessages)

from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20





# @admin.register(models.Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_per_page = 20
#     list_select_related = ['sales']
#     list_display = ['id', 'amount','created_at']

#     def amount(self, obj):
#         return obj.sales.amount


#     def items(self, obj):
#         return len(obj.sales.created_at)

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id',  'amount', 'created_at']
    list_per_page = 20
    list_select_related = ['sales']

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def amount(self, obj):
        return obj.sales.amount

  



