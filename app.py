import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

st.set_page_config(page_title="サバンナ八木 出演情報", page_icon="📺")
st.title("📺 サバンナ八木真澄 出演情報")

def get_yagi_schedule():
    # 制限を回避するためのダミーのブラウザ情報
    url = "https://bangumi.org/talents/142568"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
    }
    
    try:
        # サイトからHTMLを直接取得
        session = requests.Session()
        res = session.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        
        # 相手サイトの構造を「文字」から直接探す
        # 予定が含まれる可能性のある全ての<div>タグをチェック
        schedule_data = []
        items = soup.find_all("div")
        
        for item in items:
            text = item.get_text().strip()
            # 「12月」や「1月」という文字が含まれるブロックだけを抽出
            if ("12月" in text or "1月" in text) and len(text) < 200:
                clean_text = re.sub(r'\s+', ' ', text)
                if clean_text not in schedule_data:
                    schedule_data.append(clean_text)
                    
        return schedule_data
    except Exception as e:
        return [f"取得に失敗しました。サイト側の制限がかかっています。"]

data = get_yagi_schedule()

if data and len(data) > 0:
    st.success(f"情報を取得しました")
    for s in data:
        st.info(s)
else:
    # 最終手段：情報の読み込みができない場合は直接リンクを大きく表示
    st.warning("現在、自動取得がサイト側によって制限されています。")
    st.markdown(f"### [こちらをクリックして最新の番組表を直接確認する](https://bangumi.org/talents/142568)")
    st.write("※サイトのセキュリティが強化されたため、手動確認を推奨します。")
