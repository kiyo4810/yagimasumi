import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

# サイトの基本設定
st.set_page_config(page_title="サバンナ八木 出演情報", page_icon="📺")
st.title("📺 サバンナ八木真澄 出演情報")
st.caption("最新の地上波・BS番組情報を自動取得中")

def get_yagi_schedule():
    # 八木さんのタレントページ
    url = "https://bangumi.org/talents/142568"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        
        # サイトの構造に合わせて、番組リストの親要素から丁寧に取得
        # bangumi.orgのリスト項目を狙い撃ちします
        schedule_data = []
        
        # 番組情報の塊を探す
        items = soup.find_all("div", class_="program_list_data")
        
        if not items:
            # 別のクラス名でも探してみる（念のため）
            items = soup.select(".program_list_item")

        for item in items:
            # 余計な空白や改行を消してテキストを抽出
            text = item.get_text(separator=" ").strip()
            # 連続する空白を1つにする
            clean_text = re.sub(r'\s+', ' ', text)
            if clean_text:
                schedule_data.append(clean_text)
                
        return schedule_data
    except Exception as e:
        return [f"エラーが発生しました: {e}"]

# 実行
with st.spinner('番組表から八木さんを探しています...'):
    data = get_yagi_schedule()

if data:
    st.success(f"最新の予定が {len(data)} 件見つかりました！")
    for s in data:
        # 見やすくカード形式で表示
        with st.container(border=True):
            st.markdown(f"**{s}**")
else:
    st.warning("現在、取得できる新しい出演予定は見つかりませんでした。サイト側の更新を待つか、元のサイトを確認してください。")

st.divider()
st.write("🔗 [元の番組表サイトで詳しく見る](https://bangumi.org/talents/142568)")
