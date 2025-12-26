import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="サバンナ八木 出演情報", page_icon="📺")
st.title("📺 サバンナ八木真澄 出演情報")

def get_yagi_schedule():
    url = "https://bangumi.org/talents/142568"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # 番組情報の塊（クラス名 program_list_data）をすべて取得
        items = soup.select(".program_list_data")
        
        schedule = []
        for item in items:
            text = item.get_text(separator=" ").strip()
            if text:
                schedule.append(text)
        return schedule
    except Exception as e:
        return [f"エラーが発生しました: {e}"]

data = get_yagi_schedule()

if data:
    st.success(f"最新の予定が {len(data)} 件見つかりました")
    for s in data:
        # 見やすく枠で囲んで表示
        st.info(s)
else:
    st.warning("現在、表示できる新しい出演予定は見つかりませんでした。")

st.write("---")
st.caption("データ元: bangumi.org")
