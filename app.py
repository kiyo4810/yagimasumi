import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("サバンナ八木真澄 出演番組情報")

# 番組表からデータを取ってくる関数
def get_yagi_schedule():
    url = "https://bangumi.org/talents/142568"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    
    # ここでサイトの「番組リスト」の部分だけを狙い撃ちして抽出
    # ※サイトの構造に合わせて調整します
    items = soup.select(".program_list_item") # 例としてのクラス名
    
    schedule = []
    for item in items:
        schedule.append(item.get_text())
    return schedule

# サイトに表示
data = get_yagi_schedule()
if data:
    for s in data:
        st.write(f"📺 {s}")
else:
    st.write("現在、新しい出演予定は見つかりませんでした。")
