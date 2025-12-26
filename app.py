import streamlit as st
import requests
from bs4 import BeautifulSoup

# サイトの設定
st.set_page_config(page_title="サバンナ八木 出演情報", page_icon="📺")
st.title("📺 サバンナ八木真澄 出演情報")

def get_yagi_schedule():
    url = "https://bangumi.org/talents/142568"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # bangumi.org の番組リストの塊を特定
        # 放送日・時間・番組名が含まれる枠(program_list_data)を取得
        items = soup.select(".program_list_data")
        
        schedule = []
        for item in items:
            # 内部の余計な空白を整理してテキストを取得
            text = item.get_text(separator=" ").strip()
            # 1行にまとまりすぎないよう調整
            clean_text = " ".join(text.split())
            if clean_text:
                schedule.append(clean_text)
        return schedule
    except Exception as e:
        return [f"エラーが発生しました: {e}"]

# データの取得と表示
data = get_yagi_schedule()

if data:
    st.success(f"最新の予定が {len(data)} 件見つかりました！")
    for s in data:
        # 1件ずつカード形式で表示
        with st.expander(s[:40] + "...", expanded=True):
            st.write(s)
else:
    st.warning("現在、取得できる新しい出演予定は見つかりませんでした。サイト側の更新をお待ちください。")

st.divider()
st.caption("データ元: bangumi.org (サバンナ八木真澄 出演番組一覧)")
