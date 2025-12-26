import streamlit as st
import requests
from bs4 import BeautifulSoup

# サイトのタイトル
st.set_page_config(page_title="八木真澄 番組情報bot", page_icon="📺")
st.title("📺 サバンナ八木真澄 出演情報")
st.caption("bangumi.org から最新の地上波・BS情報を取得しています")

def get_yagi_schedule():
    url = "https://bangumi.org/talents/142568"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        
        # 番組情報が含まれる枠（カード）を特定して取得
        # bangumi.orgの構造に合わせた抽出
        programs = soup.select(".program_list_data") 
        
        schedule_list = []
        for prg in programs:
            # 日時、放送局、タイトルなどを取得
            content = prg.get_text(separator=" ").strip()
            if content:
                schedule_list.append(content)
        
        return schedule_list
    except Exception as e:
        return [f"エラーが発生しました: {e}"]

# 実行と表示
with st.spinner('最新情報を取得中...'):
    data = get_yagi_schedule()

if data:
    st.success(f"{len(data)} 件の予定が見つかりました！")
    for s in data:
        with st.chat_message("user"):
            st.write(s)
else:
    st.info("現在、表示できる新しい出演予定は見つかりませんでした。")

st.divider()
st.write("🔗 [元の番組表を確認する](https://bangumi.org/talents/142568)")
