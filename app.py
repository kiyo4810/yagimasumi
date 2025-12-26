import streamlit as st
from google import genai
import datetime

st.set_page_config(page_title="サバンナ八木 出演情報", page_icon="📺")
st.title("📺 サバンナ八木真澄 出演情報")

# APIキーの設定
api_key = st.secrets["GOOGLE_API_KEY"]
client = genai.Client(api_key=api_key)

def get_yagi_info_via_ai():
    # 今日から数日間の予定をAIに検索させる命令
    today = datetime.date.today()
    prompt = f"""
    今日（{today}）以降の、サバンナ八木真澄（八木真澄）さんのテレビ出演情報をインターネットで検索してまとめてください。
    特に、12月29日や1月2日の『BSよしもと』などの予定があれば詳しく教えてください。
    
    以下の形式で出力してください：
    【放送日】時間
    【放送局】
    【番組名】
    """
    
    try:
        # AIがネットを検索して回答を生成（Search機能を使用）
        response = client.models.generate_content(
            model='gemini-2.0-flash', # 最新の2.0なら検索能力が最強です
            contents=prompt,
            config={
                'tools': [{'google_search': {}}]
            }
        )
        return response.text
    except Exception as e:
        return f"AI検索中にエラーが発生しました: {e}"

# サイトの表示
if st.button('最新の出演情報をAIで検索する'):
    with st.spinner('AIがネット上の番組表を巡回中...'):
        result = get_yagi_info_via_ai()
        st.markdown("### ✨ AIが見つけた最新スケジュール")
        st.write(result)
else:
    st.info("上のボタンを押すと、AIが最新の予定をネットで調べて表示します。")

st.divider()
st.caption("※情報はAIが検索した結果に基づきます。正確な情報は各局の公式サイトをご確認ください。")
