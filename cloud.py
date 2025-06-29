import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import numpy as np
from PIL import Image

CSV_FILE = "song.csv"
LYRIC_COLUMN = "lyric"
OUTPUT_IMAGE = "wordcloud.png"


def load_lyrics():
    file = pd.read_csv(CSV_FILE, encoding="ANSI")

    lyrics = file[LYRIC_COLUMN].dropna().astype(str).tolist()
    return " ".join(lyrics)


def processing_lyrics(text):
    prefixes = ["作词", "作曲", "演唱", "编曲", "制作人", "歌词"]
    for prefix in prefixes:
        text = re.sub(rf"{prefix}\s*[:]\s*[\u4e00-\u9fa5]+", "", text)
    return text


def segment_text(text):
    stopwords = [
        "母带",
        "h3R3",
        "总监",
        "录音",
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
    ]  # 停用词，我根据生成后的结果手动添加进来的
    words = jieba.cut(text)
    return " ".join([word for word in words if word not in stopwords and len(word) > 1])


def generate_wordcloud(text):

    params = {
        "font_path": "simhei.ttf",
        "background_color": "white",
        "max_words": 300,
        "width": 1600,
        "height": 900,
        "collocations": False,
    }

    wordcloud = WordCloud(**params).generate(text)

    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(OUTPUT_IMAGE)
    plt.show()


lyrics = load_lyrics()
processed_lyrics = processing_lyrics(lyrics)
segmented_text = segment_text(processed_lyrics)
generate_wordcloud(segmented_text)
