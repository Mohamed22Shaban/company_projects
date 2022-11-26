from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='base'),
    path('projects/',views.Projects, name='Project'),
    path('contact/',views.contact, name='contact'),
    path('show/<int:id>',views.show, name='show'),
    # path('delete/<int:id>',views.delete, name='delete'),
    # path('contact',views.ContactView.as_view(), name='contact'),
    path('send/',views.send, name='send'),
]
