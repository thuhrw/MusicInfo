# MusicInfo

```
MusicInfo
├─ bar.py
├─ cloud.py
├─ dataanalysis.md
├─ dataanalysis.pdf
├─ download_desc.py
├─ download_img.py
├─ download_pop
│  ├─ mean.csv
│  ├─ mean.py
│  ├─ meanall.csv
│  ├─ meancopy.csv
│  ├─ pop.csv
│  ├─ popcom.py
│  ├─ popcopy.csv
│  ├─ processing.py
│  └─ result.png
├─ project1
│  ├─ manage.py
│  ├─ MUSIC
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_singer.py
│  │  │  ├─ 0003_singer_num.py
│  │  │  ├─ 0004_comment.py
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     ├─ 0001_initial.cpython-313.pyc
│  │  │     ├─ 0002_singer.cpython-313.pyc
│  │  │     ├─ 0003_singer_num.cpython-313.pyc
│  │  │     ├─ 0004_comment.cpython-313.pyc
│  │  │     └─ __init__.cpython-313.pyc
│  │  ├─ models.py
│  │  ├─ templates
│  │  │  ├─ index.html
│  │  │  ├─ index1.html
│  │  │  ├─ index2.html
│  │  │  ├─ index3.html
│  │  │  ├─ index4.html
│  │  │  └─ index5.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ admin.cpython-313.pyc
│  │     ├─ apps.cpython-313.pyc
│  │     ├─ models.cpython-313.pyc
│  │     ├─ urls.cpython-313.pyc
│  │     ├─ views.cpython-313.pyc
│  │     └─ __init__.cpython-313.pyc
│  ├─ project1
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ settings.cpython-313.pyc
│  │     ├─ urls.cpython-313.pyc
│  │     ├─ wsgi.cpython-313.pyc
│  │     └─ __init__.cpython-313.pyc
│  ├─ singerimporter.py
│  └─ songimporter.py
├─ README.md
├─ report.md
├─ report.pdf
├─ spider.py
└─ year.py
```

本项目为歌曲网站。

（1）网站构建有关的django部分的代码和html在project1文件夹中。其中singerimporter.py和songimporter.py分别为向数据库写入数据的代码。/MUSIC/templates中有所有网页的html代码。其中index为主页（歌曲列表页），index1为歌曲详情页，index2为歌手列表页，index3为歌手详情页，index4为歌手的搜索结果页，index5为歌曲的搜索结果页。

（2）cloud.py为生成词云的代码，词云为wordcloud.png。year.py为爬取歌曲年份的代码，结果在year.csv中，bar.py为生成年份的柱状图的代码，图为bar.png。download_pop为爬取热度和评论数据并进行分析的代码的文件夹，其中popcom.py为爬取数据的代码，mean.py为取均值的代码，得到meanall.csv，然后为了数据分析只选择了41位歌手得到mean.csv, 在csv中利用excel里的函数处理数据得到meancopy.csv，然后利用meancopy.csv通过processing.py进行分析，结果为result.png

（3）spider.py为主爬虫程序，然后由于网站反爬的问题，所以实际爬虫时利用了download_desc.py（爬取歌手简介），download_img.py（爬取歌曲图片）等代码进行补爬，最后将数据汇总在song.csv和singer.csv中。歌手和歌曲图片分别在singerpics和songpics文件夹中。

（4）数据分析报告为dataanalysis.pdf。实验报告为report.pdf