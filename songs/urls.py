from django.urls import path

from . import views

app_name = 'songs'
urlpatterns = [
    #/songs/
    path('/', views.index, name='index'),
]
