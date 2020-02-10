from django.urls import path

from . import views

urlpatterns = [
    path('',views.api, name='api'),
    path('getgit', views.getgit, name='gitdata' ),
    path('getword', views.getword, name='owlbot')
]