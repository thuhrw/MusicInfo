from django.urls import path, include
import MUSIC.views as views

urlpatterns = [
    path("MUSIC/<int:id>", views.show_song),
    path("MUSIC", views.show_mainpage),
    path("MUSIC/artist", views.show_artistlist),
    path("MUSIC/artist/<int:id>", views.show_singer),
    path("comment/<int:id>", views.comment),
    path("delcomment/<int:id>", views.delcomment),
]
