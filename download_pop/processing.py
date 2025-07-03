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
