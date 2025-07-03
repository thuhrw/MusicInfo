from django.shortcuts import render
from django.conf import settings
from .models import Song, Singer, Comment
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
import time


def show_song(request, id):
    """展示歌曲信息,在数据库中滤出这首歌的所有评论数据"""
    song = Song.objects.get(id=id)
    artist = Singer.objects.get(name=song.artist)
    artistid = artist.id
    comments = Comment.objects.filter(num=id)

    return render(
        request,
        "index1.html",
        {
            "song": song,
            "MEDIA_URL": settings.MEDIA_URL,
            "artistid": artistid,
            "comments": comments[::-1],
        },
    )


def show_singer(request, id):
    """展示歌手信息,在数据库中滤出歌手的歌曲"""
    singer = Singer.objects.get(id=id)
    song_list = Song.objects.filter(artist=singer.name)

    return render(
        request,
        "index3.html",
        {"singer": singer, "MEDIA_URL": settings.MEDIA_URL, "song_list": song_list},
    )


def show_mainpage(request):
    """歌曲详情页"""
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
    """歌手列表页"""
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
        "index2.html",
        {"singers": singers, "base_url": base_url, "MEDIA_URL": settings.MEDIA_URL},
    )


def comment(request, id):
    """评论函数"""
    content = request.POST.get("content")
    obj = Comment(num=id, context=content)
    obj.full_clean()
    obj.save()
    return HttpResponseRedirect(f"/index/MUSIC/{id}")


def delcomment(request, id):
    """删除评论"""
    iden = request.POST.get("delete_comment")
    comment = Comment.objects.get(id=iden)
    comment.delete()
    return HttpResponseRedirect(f"/index/MUSIC/{id}")


def search(request):
    """搜索"""
    query = request.GET.get("q")
    search_type = request.GET.get("type")
    if search_type == "artist":
        start_time = time.time()
        singer_list = Singer.objects.filter(
            Q(name__contains=query) | Q(desc__contains=query)
        )
        end_time = time.time()
        lens = len(singer_list)

        paginator = Paginator(singer_list, 8)

        page = request.GET.get("page")
        try:
            singers = paginator.page(page)
        except PageNotAnInteger:
            singers = paginator.page(1)
        except EmptyPage:
            singers = paginator.page(paginator.num_pages)

        base_url = "/index/search?type=artist&q=" + query

        return render(
            request,
            "index4.html",
            {
                "singers": singers,
                "base_url": base_url,
                "MEDIA_URL": settings.MEDIA_URL,
                "query": query,
                "time": "{:.5f}".format(end_time - start_time),
                "len": lens,
            },
        )

    if search_type == "song":
        start_time = time.time()
        song_list = Song.objects.filter(
            Q(name__contains=query)
            | Q(artist__contains=query)
            | Q(lyric__contains=query)
        )
        end_time = time.time()
        lens = len(song_list)
        paginator = Paginator(song_list, 8)

        page = request.GET.get("page")
        try:
            songs = paginator.page(page)
        except PageNotAnInteger:
            songs = paginator.page(1)
        except EmptyPage:
            songs = paginator.page(paginator.num_pages)

        base_url = "/index/search?type=song&q=" + query

        return render(
            request,
            "index5.html",
            {
                "songs": songs,
                "base_url": base_url,
                "MEDIA_URL": settings.MEDIA_URL,
                "query": query,
                "time": "{:.5f}".format(end_time - start_time),
                "len": lens,
            },
        )
