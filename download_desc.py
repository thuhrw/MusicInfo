import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cookie": "_iuqxldmzr_=32; _ntes_nnid=bb7109532e8d77c77aef7bbaa5e2fe17,1750913979603; _ntes_nuid=bb7109532e8d77c77aef7bbaa5e2fe17; NMTID=00OXkNQnih9-_wL80hDlFKOp8snELAAAAGXqpsaKQ; WEVNSM=1.0.0; WNMCID=yabfrq.1750913981014.01.0; WM_TID=vfNHnE6%2B7TVEBBFFAEeHa42dgt8dWCwT; sDeviceId=YD-UxDDLAnk%2B7FEB1RVUEKSLtiMkt4NYjxo; ntes_utid=tid._.iVp8ctmGsOdEVkFQQVKCP4mJl9pINz08._.0; __snaker__id=Q9gCRc1mDTbCaLWB; gdxidpyhxdE=NTrx%2FtT95NTQv%2FjQvqx%2FTsfNd4oNx2tNxJClzfub29pQ8ziRs975yi2%2BTsCpiJmufRyTtJx2D%5CoiNY00a%2B%5Cv8%5CLVJsyMfgN%2BfMJd%5CGn292ltbwsTdrbjuXGCIiXKm%5Cgp9komJwx5J%2FMrQAIjUH%2FVHbsNpmvJW3O8I8v6cGcNIzQ5HOx%2B%3A1750924972906; P_INFO=18964713033|1750924140|1|music|00&99|null&null&null#bej&null#10#0|&0||18964713033; __remember_me=true; MUSIC_U=0062764A5157727444AAEA8D849B30CD1C19BA7858B4EDBD60436C74028733A55886430B9BF0969FDA9101DE079295F1D165F7F00B0C7033CE222B2D4351618A29A6897E6094D189554417A4BCEED710A0BD7E832339A0941248D73DFB5C6F894CC4BB0A75C2DF1A559CDE1E579023046085FF34F8061D82B5F85F049A3149420E60470BF90BE73E1B9B461B389CBCB63883D1A00E137440A9E0409AD28A0F27E72FC74BD536F509043FA31DAFEE06960B79AE4998E1D3DA31AA6FA0B6E2F0AD21113F605419EA5F96DF01507B1324E73367921B9A0A51B32A4307F41701C1B67D36E14878CF47864DBD694825F4F4D6DDEC56F02A52A7844689F7CCCD4CE8D7C6A61DAEFB04782402B9691A2E52099CDA6662066ED29E26A286B6D781ED11265EB25B8371C7926B67EE51BC59A99A3D77A2E943347C1D34E9037343DABF6F6254028AA812489F64294A216DD70B067BF3D76CD1B0FB778DC21AB22AE2D2FC91C3; __csrf=f20a86e42b87a7983d46ed59d236f49b; ntes_kaola_ad=1; JSESSIONID-WYYY=l%5CTGofQaOo%5CH0%2BUOb%2BC%2FnJB%2FV5Bg6ei6aXowV8Zc3as%2B74C9J61GT%5C0Q1O%2BVxrQeFFpgP46TIo2EEYzS3bnPo204Ot%5CHpp9%5CaC7y4HzV2pJ%2FpE%5C3qYKpoDF4HmcXaQuJtb86dOEpAe%2F8FRchVcVHh4AYNYTN%2FafKjE7BQzU40575NNtg%3A1750992559822; WM_NI=mti%2B1GNynSdwPEJ1%2BKWMTTGxl1lFl41%2B9o7EncaIbfz9qPQYbwfDwiWzZEwWLtPe1dnxlA0x4pIWHi6IspSsh%2BO9V4Hftk%2BCKWmCe%2F5kwtsOnUeaccdY1wplDP1MpKt8bEY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee99ae4fabb8a294cf3392968bb2c85e928f8e86cb6ab1a7bfb4e867948aa392aa2af0fea7c3b92aafaca7ccb44d8ea7a2b4e77d949b86d2aa4195939cb5c674b0efa4a7ef40f3f5f790b64faebdafaae16ebae7bfb1d453a2a9aaa5f66395a696a6f65d90aca086b470aea8a4a2b374f8b087b8cb63f697bd91d279acf581dad5408cbabc8caa498989a3a4e825f7b5b995f245ae8bab82e269a887ff98f3688890ffaef341b8e8aea6dc37e2a3",
    "referer": "https://music.163.com/",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
}


csvfile = open(r"C:\Users\14395\Desktop\git\MusicInfo\singer.csv", "r", errors="ignore")
file = open(r"C:\Users\14395\Desktop\git\MusicInfo\desc.csv", "a", errors="ignore")
reader = csv.DictReader(csvfile)
writer = csv.writer(file)

for row_num, row in enumerate(reader):
    if row_num % 2 == 0:
        continue

    id = row["artist_id"]
    url = "https://music.163.com/artist/desc?id=" + id

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "lxml")

    intro_div = soup.find("div", class_="n-artdesc")  # 按class查找
    first_paragraph = intro_div.find("p")
    intro_text = first_paragraph.get_text(strip=False).strip()
    writer.writerow((intro_text,))
