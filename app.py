import streamlit as st
import google.generativeai as genai
import datetime

# サイトの基本設定
st.set_page_config(page_title="サバンナ八木 出演情報", page_icon="📺")
st.title("📺 サバンナ八木真澄 出演情報")

# APIキーの設定
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("APIキーの設定が見つかりません。")

def get_yagi_info_via_ai():
    today = datetime.date.today()
    # 安定版の1.5-flashを直接指定
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    サバンナ八木真澄（八木真澄）さんの今日（{today}）以降のテレビ出演情報をネットで検索してまとめてください。
    特に12月29日や1月2日のBSよしもと、その他の特番情報を優先して探してください。
    
    出力形式：
    【放送日】時間
    【放送局】
    【番組名】
    """
    
    try:
        # 検索ツール（google_search）を使って回答を生成
        # この書き方が最もエラーが起きにくい世界標準の形式です
        response = model.generate_content(
            prompt,
            tools=[{"google_search_retrieval": {}}]
        )
        return response.text
    except Exception as e:
        return f"AI検索中にエラーが発生しました。1分待って再試行してください: {e}"

# 画面表示
st.info("AIがネット上の最新番組表をリアルタイムで検索します。")

if st.button('最新の出演情報をAIで検索する'):
    with st.spinner('八木さんの最新情報を調査中...'):
        result = get_yagi_info_via_ai()
        st.markdown("### ✨ AIが見つけた最新スケジュール")
        st.write(result)

st.divider()
st.caption(f"検索実行日: {datetime.date.today()}")
