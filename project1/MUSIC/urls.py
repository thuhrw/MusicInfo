from django.urls import path, include
import MUSIC.views as views

urlpatterns = [
    path("MUSIC/<int:id>", views.show_song),
    path("MUSIC", views.show_mainpage),
    path("MUSIC/artist", views.show_artistlist),
]
