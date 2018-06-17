from django.urls import path

from . import views
import songs.views

app_name = 'songs'
urlpatterns = [
    path('', songs.views.index, name='index'),
]
