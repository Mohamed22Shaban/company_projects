from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='base'),
    path('projects/',views.Projects, name='Project'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('register/<int:id>',views.delete, name='register'),
    path('send',views.send, name='send'),
]
