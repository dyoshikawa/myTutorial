from django.urls import path

from . import views

app_name = 'songs'
urlpatterns = [
    url('songs/', views.index, name='index'),
]
