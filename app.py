import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="サバンナ八木 応援ポータル", page_icon="🇧🇷")

# 2. 画像URL
yagi_url = "https://raw.githubusercontent.com/kiyo4810/yagimasumi/main/images/yagi_bg.jpg"

# 3. 背景と文字色の設定（ダークモード対策）
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)), 
                          url("{yagi_url}");
        background-repeat: no-repeat !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}
    /* すべてのテキストを黒系に固定 */
    .stApp * {{
        color: #222222 !important;
    }}
    /* ボタン内の文字色を維持 */
    .stButton button p, .stLinkButton a span {{
        color: inherit !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 4. コンテンツ開始
st.title("🇧🇷 サバンナ八木 応援ポータル")
st.write("最新情報をチェックして、みんなで応援しましょう！")

st.divider()

# --- セクション 1 ---
st.header("1. 🗓️ 最新のテレビ出演情報")
st.link_button(
    "👉 番組表を別タブで開く", 
    "https://bangumi.org/talents/142568",
    type="primary",
    use_container_width=True
)

st.divider()

# --- セクション 2 ---
st.header("2. 💰 stand.fm お金のしゃべり場")
st.components.v1.iframe("https://stand.fm/embed/channels/674833f669bc2015d09df281", height=450)
st.link_button(
    "📻 stand.fm 公式サイトへ", 
    "https://stand.fm/channels/674833f669bc2015d09df281",
    use_container_width=True
)

st.divider()

# --- セクション 3 ---
st.header("3. 🎙️ YouTube 芸人男塾")
st.video("https://www.youtube.com/watch?v=q10EVteYbgw")
st.link_button(
    "🏮 YouTube チャンネルへ（直リンク）", 
    "https://www.youtube.com/channel/UCYhNHFMZZ7gGal-RLCm_65Q", 
    use_container_width=True
)

st.divider()

# --- セクション 4 ---
st.header("4. 🇧🇷 ブラジルの人へ")
if st.button("ブラジルの人、聞こえますかー！", use_container_width=True):
    st.balloons()
    st.success("「聞こえたよー！」（ブラジルの裏側より）")
