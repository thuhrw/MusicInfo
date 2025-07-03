import pandas as pd

import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]


data = pd.read_csv(r"C:\Users\14395\Desktop\git\MusicInfo\year.csv")

data = data.dropna()


plt.figure(figsize=(16, 8))
bars = plt.bar(data["year"].astype(int).astype(str), data["count"])


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
