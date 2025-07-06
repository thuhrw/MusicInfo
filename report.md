# 实验报告

## 一、网页系统功能

### （i）class

```python
from django.db import models
from django.utils import timezone


class Song(models.Model):
    num = models.IntegerField()
    name = models.CharField()
    artist = models.CharField()
    lyric = models.CharField()
    url = models.CharField()
    pic_url = models.CharField()
    artist_url = models.CharField()


class Singer(models.Model):
    num = models.IntegerField()
    name = models.CharField()
    pic_url = models.CharField()
    desc = models.CharField()
    url = models.CharField()


class Comment(models.Model):
    num = models.IntegerField()
    context = models.CharField()
    created_at = models.DateTimeField(default=timezone.now)

```
歌曲类成员变量有num(编号)，name(歌曲名)，artist(歌手名)，lyric(歌词)，url(原网站链接)，pic_url(歌曲图片url)，artist_url(歌手图片的url)。歌手类成员变量有num(编号)，name(歌手名)，pic_url(图片的url)，url(原网站链接)，desc(歌手简介)。评论类成员变量有num(对应歌曲的编号)，context(正文)，created_at(时间)。


###(ii)页面
####1.主页（歌曲列表页）

<img src="C:\Users\14395\Desktop\git\MusicInfo\mainpage.png">

<img src="C:\Users\14395\Desktop\git\MusicInfo\mainpage1.png">

该页面为歌曲列表页。点击“Artist Library”可以切换到歌手列表页。此页面上具有搜索功能，输入非空搜索内容后点击搜索之后的画面就是搜索结果页。可以从此页面跳转到歌手列表页和歌曲详情页。分页跳转功能支持输入页数和按键增加减少两种方式。背景为45度的渐变颜色，搜索按钮颜色为初音未来色和清华紫的渐变。图标样式来自于font-awesome。

```python
def show_mainpage(request):
    """歌曲详情页

    每页显示8首歌曲,如果用户输入的页数不是整数就跳转到第一页，如果超出范围则跳转到最近的页数
    """
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
```

获得所有歌曲，并进行分页，解析index.html并传入一些参数，base_url为跳转服务，MEDIA_URL为本地资源的文件夹

#### 2、歌曲详情页

<img src="C:\Users\14395\Desktop\git\MusicInfo\songdetail.png">

<img src="C:\Users\14395\Desktop\git\MusicInfo\songdetail1.png">

此页面点击歌手名可以跳转到歌手详情页，点击url跳转到原网站，点击Back返回歌曲列表页。评论提交内容不能为空。

```python
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
```

获取这一首歌曲，及对应的评论，转换为倒序列表作为参数，解析index1.html



#### 3、歌手列表页

<img src="C:\Users\14395\Desktop\git\MusicInfo\artistlibrary.png">

页面功能和歌曲列表页一样

```python
def show_artistlist(request):
    """歌手列表页

    每页显示8位歌手,如果用户输入的页数不是整数就跳转到第一页，如果超出范围则跳转到最近的页数
    """
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
```



#### 4、歌手详情页

<img src="C:\Users\14395\Desktop\git\MusicInfo\singerdetail.png">

点击url跳转到原歌手网页，点击Back返回歌手列表页。点击歌曲封面和歌曲名可以跳转到歌曲列表页

```python
def show_singer(request, id):
    """展示歌手信息,在数据库中滤出歌手的歌曲"""
    singer = Singer.objects.get(id=id)
    song_list = Song.objects.filter(artist=singer.name)

    return render(
        request,
        "index3.html",
        {"singer": singer, "MEDIA_URL": settings.MEDIA_URL, "song_list": song_list},
    )
```





####5、搜索结果页

<img src="C:\Users\14395\Desktop\git\MusicInfo\searchresult.png">

与歌曲列表页和歌手列表页一致，仅增加了搜索结果与搜索时间。点击对应卡片可以跳转到详情页

```python
def search(request):
    """搜索

    搜索时间为filter的查询时间
    通过传进来的type参数，进行不同的搜索，并且解析不同的html页面
    """
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
```

通过搜索页面传进来的类型参数在数据库中搜索结果，搜索时间认为是filter函数的时间，保留5位小数，len为结果的数量

## 二、数据量

#### 歌曲：2026首；歌手100位

## 三、使用的技术与算法

#### (1)使用songimporter.py和singerimporter.py向数据库中导入数据

```python
import os
import sys
import csv
import django


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1.settings")
django.setup()

from MUSIC.models import Singer


def func():
    """将歌手信息导入数据库"""

    singerfile = open(r"C:\Users\14395\Desktop\git\MusicInfo\singer.csv", "r")

    singreader = csv.DictReader(singerfile)
    for row_num, row in enumerate(singreader):
        if row_num % 2 == 0:
            continue

        singer = Singer(
            num=row["artist_id"],
            name=row["artist_name"],
            pic_url=row["artist_pic_url"],
            desc=row["artist_desc"],
            url=row["artist_url"],
        )

        singer.save()


func()
print(f"成功导入 {Singer.objects.count()} 个歌手")

```

```python
import os
import sys
import csv
import django


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1.settings")
django.setup()

from MUSIC.models import Song


def func():
    """将歌曲信息导入数据库"""
    csvfile = open(r"C:\Users\14395\Desktop\git\MusicInfo\song.csv", "r")
    singerfile = open(r"C:\Users\14395\Desktop\git\MusicInfo\singer.csv", "r")
    reader = csv.DictReader(csvfile)
    singreader = csv.DictReader(singerfile)
    for row_num, row in enumerate(reader):
        if row_num % 2 == 0:
            continue

        tmp = row["artist_name"]
        singer_url = ""
        for hang in singreader:
            if hang["artist_name"] == tmp:
                singer_url = hang["artist_url"]
                break

        song = Song(
            num=row["song_id"],
            name=row["song_name"],
            artist=row["artist_name"],
            lyric=row["lyric"],
            url=row["song_url"],
            pic_url=row["song_pic"],
            artist_url=singer_url,
        )
        song.save()


func()
print(f"成功导入 {Song.objects.count()} 首歌曲")
```

#### (2)评论采用网页重定向

```python
def comment(request, id):
    """评论函数"""
    content = request.POST.get("content")
    obj = Comment(num=id, context=content)
    obj.full_clean()  # 进行数据验证
    obj.save()
    return HttpResponseRedirect(f"/index/MUSIC/{id}")


def delcomment(request, id):
    """删除评论"""
    iden = request.POST.get("delete_comment")
    comment = Comment.objects.get(id=iden)
    comment.delete()
    return HttpResponseRedirect(f"/index/MUSIC/{id}")
```

####（3）利用jieba库处理歌词

```python
def segment_text(text):
    """由于歌曲的信息各不相同，所以前面处理歌词的函数会有遗漏。手动根据词云结果添加停用词

    Keyword arguments:
    text -- 字符串

    返回处理后的字符串
    """
    stopwords = [
        "母带",
        "h3R3",
        "总监",
        "录音",
        "制作",
        "录音师",
        "作词",
        "出品人",
        "网易",
        "法老",
        "陶喆",
        "Producer",
        "编曲",
        "SBMS",
        "配唱",
        "版权",
        "国际",
        "弦乐",
        "贝斯",
        "Studio21A",
        "统筹",
        "录音室",
        "编写",
        "键盘",
        "NEWBAND",
        "公司",
        "音频编辑",
        "钢琴",
        "维伴",
        "首席",
        "乐队",
        "音响",
        "原唱",
        "编曲",
        "作曲",
        "Ltd",
        "打击乐",
        "Sound",
        "rapper",
        "Music",
        "混音",
        "牛班",
        "吉他",
        "音乐",
        "Studio",
        "Engineer",
        "Publishing",
        "何飚",
        "don",
        "PGM",
        "Vocal",
        "有限公司",
        "工作室",
        "林俊杰",
        "队长",
        "Asen",
        "罗言",
        "re",
        "乐团",
        "人声",
        "企划",
        "MUSIC",
        "项目",
        "Wiz",
        "OP",
        "录音棚",
        "汪苏",
        "郎梓朔",
        "营销",
        "发行",
        "Program",
        "编辑",
        "石行",
        "改编",
        "工程师",
        "爱乐乐团",
        "监制",
        "Mixing",
        "说唱",
        "SP",
        "Mastering",
        "Chan",
        "张子",
        "陈楚生",
        "刘卓",
        "索尼",
        "林梦洋",
        "设计",
    ]
    words = jieba.cut(text)
    return " ".join([word for word in words if word not in stopwords and len(word) > 1])
```

#### (4)利用adjustText库处理散点图的名称标签，避免重合

```python
texts = []
for i, artist in enumerate(artists):
    texts.append(plt.text(x.iloc[i], y.iloc[i], artist, fontsize=6, alpha=1))


adjust_text(
    texts,
    expand_points=(2, 2),
    expand_text=(1.2, 1.2),
    force_text=(0.5, 0.5),
    only_move={"points": "y", "text": "y"},
)
```

#### (5)其他技术：pandas，matplotlib，re，requests，BeautifulSoup等技术





## 四、实验用时与感想

#### (1)爬虫且完整获得数据：36h

####(2)网页系统设计：36h

#### (3)数据分析：24h

#### 感想：这是第一个我完成的计算机技术工程，颇有成就感。从一开始畏惧网页复杂的html源码，到熟练的找到所需内容，从一开始总是写成c++到掌握python的基础语法，第一次写html构建网站都让我收获良多。总的来说，这次实验的内容非常不错，让我掌握了许多重要的技术和技能。任务量有一点小大:(

