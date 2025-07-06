import pandas as pd


df = pd.read_csv(
    r"C:\Users\14395\Desktop\git\MusicInfo\download_pop\popcopy.csv",
    skip_blank_lines=True,
    encoding="ANSI",
)


artist_stats = (
    df.groupby("artist_name").agg({"pop": "mean", "comment": "mean"}).reset_index()
)


artist_stats.columns = ["artist_name", "avg_pop", "avg_comment"]


artist_stats.to_csv(
    r"C:\Users\14395\Desktop\git\MusicInfo\download_pop\meanall.csv", index=False
)
