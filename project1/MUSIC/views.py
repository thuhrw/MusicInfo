from django.shortcuts import render
from django.conf import settings
from .models import Song, Singer
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


def show_song(request, id):
    song = Song.objects.get(id=id)

    return render(
        request, "index4.html", {"song": song, "MEDIA_URL": settings.MEDIA_URL}
    )


def show_mainpage(request):
    song_list = Song.objects.all()
    paginator = Paginator(song_list, 8)

    page = request.GET.get("page")
    try:
        songs = paginator.page(page)
    except PageNotAnInteger:

        songs = paginator.page(1)
    except EmptyPage:

        songs = paginator.page(paginator.num_pages)

    base_url = "/index/MUSIC"
    return render(
        request,
        "index.html",
        {"songs": songs, "base_url": base_url, "MEDIA_URL": settings.MEDIA_URL},
    )


def show_artistlist(request):
    singer_list = Singer.objects.all()
    paginator = Paginator(singer_list, 8)

    page = request.GET.get("page")
    try:
        singers = paginator.page(page)
    except PageNotAnInteger:

        singers = paginator.page(1)
    except EmptyPage:

        singers = paginator.page(paginator.num_pages)
    base_url = "/index/MUSIC/artist"

    return render(
        request,
        "index5.html",
        {"singers": singers, "base_url": base_url, "MEDIA_URL": settings.MEDIA_URL},
    )


# def comment(request, id):
#     data = request.POST
#     # 将新的消息添加到数据库中
#     user = data["user"]
#     comment_content = data["content"]
#     blog = Blog.objects.get(id=id)
#     obj = Comment(blog=blog, user=user, comment_content=comment_content)
#     obj.full_clean()  # 对数据进行验证
#     obj.save()  # 存储在表中
#     return HttpResponseRedirect(f"/index/blog/{id}")  # 将页面重定向到博客的url
