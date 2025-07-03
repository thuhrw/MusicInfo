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
    """_summary_
    将歌手信息导入数据库
    """

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
