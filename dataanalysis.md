# 数据分析1：热词词云与主题分析

<img src="C:\Users\14395\Desktop\git\MusicInfo\wordcloud.png">

####结论（论证）：从词云看，热门歌曲主题常围绕情感抒发（喜欢、幸福、思念、孤独、回忆、baby、girl、love等）、成长感悟（青春、遗憾等）、生活哲思（时间、世界、生命、岁月等）展开 。情歌仍然是华语乐坛目前最流行的主题类型。

#### 结论的意义：掌握华语音乐的流行风向标，明确热门主题，如情感、成长、生活哲思等，创作者可依此精准选题，让作品更贴合大众情绪需求，提升传播潜力，像聚焦青春遗憾的歌，易引发年轻听众共鸣 。创新性：利用客观数据，避免听众的主观判断，选择华语热歌榜避免了不同听众的对其他因素（如旋律）的喜好对结论的影响。

```python
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

# 解释器选择全局


def load_lyrics():
    """将所有歌词加载进来,作为一个字符串"""
    file = pd.read_csv(CSV_FILE, encoding="ANSI")

    lyrics = file[LYRIC_COLUMN].dropna().astype(str).tolist()
    return " ".join(lyrics)


def processing_lyrics(text):
    """处理歌词,去掉一部分信息
    
    Keyword arguments:
    text -- 所有歌词形成的字符串
    
    返回处理后的字符串
    """
    prefixes = ["作词", "作曲", "演唱", "编曲", "制作人", "歌词"]
    for prefix in prefixes:
        text = re.sub(rf"{prefix}\s*[:]\s*[\u4e00-\u9fa5]+", "", text)
    return text


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
        "制作"，
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


def generate_wordcloud(text):
    """生成词云
    
    Keyword arguments:
    text -- 字符串
    """

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

```





# 数据分析2：流行歌曲年份

<img src="C:\Users\14395\Desktop\git\MusicInfo\bar.png">

####结论：总体上来说，越新的歌曲流行程度越高。但是在其中也有个别年份热门歌曲数量较高如2000、2003、2007、2010、2011、2016等，这说明听众仍然有相当高的比例喜欢听较老的歌曲，这些歌曲凭借其高质量成为经典永流传。

####结论的意义与创新性：网络上总是流传着华语乐坛青黄不接的言论。通过数据我们可以看到，虽然一些高质量的歌曲仍然在今天保持很高的热度，但是听众仍然较为喜欢听新歌，对这些歌曲有比较强烈的喜爱。一定程度上否定了“近几年没有什么喜欢的歌曲”的言论。那么华语乐坛的青黄不接的现象，则应指代歌曲的质量下降，但是听众仍然保持高喜爱，高质量的经典老歌与之相比热度较低，一定程度上反映了听众审美的降级。

```python
import pandas as pd

import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]


data = pd.read_csv(r"C:\Users\14395\Desktop\git\MusicInfo\year.csv")

data = data.dropna()


plt.figure(figsize=(16, 8))
bars = plt.bar(
    data["year"].astype(int).astype(str), data["count"]
)  # 数据导入时会变成2024.0，所以我先转成整数在转成字符串


for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0,
        height + 5,
        f"{int(height)}",
        ha="center",
        va="bottom",
        fontsize=9,
        rotation=45,
    )


plt.title("热门歌曲分布 (1986-2025)", fontsize=16, pad=20)
plt.xlabel("年份", fontsize=12)
plt.ylabel("数量", fontsize=12)
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=1)


plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

plt.savefig("bar.png", dpi=300)


plt.show()
```

# 数据分析3：粉丝忠实度与活跃度

<img src="C:\Users\14395\Desktop\git\MusicInfo\download_pop\result.png">

##！！！注意图表横坐标不是从0开始

####结论(论证)：许嵩、薛之谦、郭顶、华晨宇等歌手的歌曲质量较高，容易打动人。而DJ阿智等歌手的作用与听众建立情感链接的程度较低。斜率表明在单位热度下歌手的评论数量，斜率越大则表明这首歌的听众更愿意为这个歌手评论，有深刻的情感共鸣，斜率越高的点听众忠实度与活跃度越高。通过爬虫获得的pop指数和评论数构建流行指数。因为评论数与时间长度有关，采用对数函数将其映射到0-100的区间，与pop指数加权平均得到流行指数。而评论指数则是通过评论数量直接映射到0-100。

#### 结论的意义与创新性：一首歌曲或是一位歌手不能只看他的热度。有的网红获得了很大的关注，但是其本身的作品质量并不高。通过粉丝活跃度与听众与歌曲产生深刻情感共鸣的比例，可以筛选出真正优秀热门的歌手。这种方式相比于简单的看播放量或则较为困难的歌曲评奖，能较为准确简单的筛选出优秀的歌手与作品，具有创新性。



```python
import pandas as pd
import matplotlib.pyplot as plt
from adjustText import adjust_text

# 解释器选择全局

file_path = r"C:\Users\14395\Desktop\git\MusicInfo\download_pop\meancopy.csv"
df = pd.read_csv(file_path, encoding="utf-8")

# 在meancopy里，评论指数是min(评论数/1000,100),流行指数结合爬到的pop和评论数量数据，进行加权平均
# 由于网易云中pop的数据有上限100，大量歌手的pop数据，都是100，因此我降低了权重，为0.3，评论数作为热度的一部分，权重为0.7
# 将评论数通过函数映射到0-100的得分区间内


x = df["process_pop"]
y = df["process_com"]
artists = df["artist_name"]


plt.figure(figsize=(16, 12))
plt.scatter(x, y, alpha=1, color="#39c5bb", edgecolor="w", s=60)  # miku 应援色

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]


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


plt.xlabel("流行指数", fontsize=13, fontweight="bold")
plt.ylabel("评论指数", fontsize=13, fontweight="bold")
plt.title("歌手流行指数与评论指数关系图", fontsize=16, fontweight="bold")
plt.grid(True, linestyle="--", alpha=0.2)


plt.gca().set_facecolor("#f8f9fa")


output_path = r"C:\Users\14395\Desktop\git\MusicInfo\download_pop\result.png"
plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches="tight", facecolor="white")

plt.show()

```

