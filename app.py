import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

st.set_page_config(page_title="サバンナ八木 出演情報", page_icon="📺")
st.title("📺 サバンナ八木真澄 出演情報")

def get_yagi_schedule():
    url = "https://bangumi.org/talents/142568"
    # 人間がブラウザでアクセスしているように見せかける高度なヘッダー
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
        "Referer": "https://www.google.com/"
    }
    
    try:
        # セッションを使ってアクセスを安定させる
        session = requests.Session()
        res = session.get(url, headers=headers, timeout=15)
        res.encoding = res.apparent_encoding # 文字化け防止
        
        soup = BeautifulSoup(res.text, "html.parser")
        
        # 【戦略】特定のタグを探すのではなく、テキスト全体から「日付＋番組」っぽい部分を抽出
        raw_text = soup.get_text(separator="\n")
        lines = raw_text.split('\n')
        
        extracted = []
        for line in lines:
            line = line.strip()
            # 「12/29」や「12月29日」や「1月」という文字が含まれる行を拾う
            if re.search(r'(\d{1,2}/\d{1,2}|\d{1,2}月\d{1,2}日)', line):
                # 短すぎず長すぎない、意味のありそうな行だけを採用
                if 10 < len(line) < 200:
                    extracted.append(line)
        
        # 重複を削除
        return list(dict.fromkeys(extracted))
        
    except Exception as e:
        return [f"取得エラーが発生しました: {e}"]

# データの取得と表示
with st.spinner('番組表のガードを突破して読み込み中...'):
    data = get_yagi_schedule()

if data:
    st.success(f"最新の番組情報を見つけました！")
    for s in data:
        st.info(s)
else:
    st.warning("現在、自動取得がサイト側にブロックされているか、予定が掲載されていません。")
    st.markdown(f"### 💡 [ここをクリックして公式サイトを直接確認](https://bangumi.org/talents/142568)")
    st.write("※公式サイトに予定があるのにここに表示されない場合は、セキュリティ制限が原因です。")

st.divider()
st.caption("データ取得元: bangumi.org")
