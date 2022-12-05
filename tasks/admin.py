from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Clients)
# admin.site.register(EmailSender)
admin.site.register(EmailSubscribe)
# admin.site.register(Project)
admin.site.register(Sales)
admin.site.register(RecievMessages)
admin.site.register(Order)

from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id','name','order']



@admin.register(models.EmailSender)
class EmailSenderAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id','title','content', 'date_added']






@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_select_related = ['category']
    list_display = ['id','name','cost', 'amount','created_at']

  
# @admin.register(models.Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id',  'amount', 'payment_method','created_at']
#     list_per_page = 20
#     list_select_related = ['sales']

#     def has_change_permission(self, request, obj=None):
#         return False

#     def has_add_permission(self, request):
#         return False

#     def amount(self, obj):
#         return obj.sales.amount

#     def payment_method(self, obj):
#         return obj.transaction.get_payment_method_display()



