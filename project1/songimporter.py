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
    """_summary_
    将歌曲信息导入数据库
    """
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
