import streamlit as st
from google.genai import Client
import datetime

# サイトの基本設定
st.set_page_config(page_title="サバンナ八木 出演情報", page_icon="📺")
st.title("📺 サバンナ八木真澄 出演情報")

# APIキーの設定（Secretsから読み込み）
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    client = Client(api_key=api_key)
except Exception as e:
    st.error("APIキーの設定が見つかりません。Settings > Secrets を確認してください。")

def get_yagi_info_via_ai():
    # 今日から数日間の予定をAIに検索させる命令
    today = datetime.date.today()
    prompt = f"""
    今日（{today}）以降の、サバンナ八木真澄（八木真澄）さんのテレビ出演情報をインターネット（番組表サイトなど）で検索して箇条書きでまとめてください。
    特に、12月29日や1月2日の『BSよしもと』の番組、その他地上波の特番予定があれば詳しく教えてください。
    
    以下の形式で出力してください：
    【放送日】時間
    【放送局】
    【番組名】
    """
    
    try:
        # 安定版の1.5-flashモデルを使用して検索
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt,
            config={
                'tools': [{'google_search': {}}]
            }
        )
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⚠️ AIが少し混み合っています。1分ほど待ってからもう一度お試しください。"
        return f"AI検索中にエラーが発生しました: {e}"

# 画面の表示
st.info("AIがネット上の最新番組表をリアルタイムで検索します。")

if st.button('最新の出演情報をAIで検索する'):
    with st.spinner('八木さんの最新情報をネットで調査中...'):
        result = get_yagi_info_via_ai()
        st.markdown("### ✨ AIが見つけた最新スケジュール")
        st.write(result)
else:
    st.write("ボタンを押して検索を開始してください。")

st.divider()
st.caption(f"検索実行日: {datetime.date.today()}")
st.caption("※AIの検索結果は100%正確ではない場合があります。公式な情報は各テレビ局の番組表をご確認ください。")
