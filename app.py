import streamlit as st

st.set_page_config(page_title="サバンナ八木 応援ポータル", page_icon="🇧🇷")

# --- 画像URLの設定 ---
yagi_url = "https://raw.githubusercontent.com/kiyo4810/yagimasumi/main/images/yagi_bg.jpg"

# --- 【最終安定版】CSS設定 ---
st.markdown(
    f"""
    <style>
    /* 1. 背景の繰り返しを徹底的に禁止し、1枚を画面に固定 */
    /* stAppだけでなく、中身の各レイヤーも透明化して背景を1枚に見せます */
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)), 
                          url("{yagi_url}") !important;
        background-repeat: no-repeat !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* 2. ダークモード・ノーマルモード共通の文字色対策 */
    .stApp * {{
        color: #222222 !important;
    }}

    /* 3. ボタン内の文字を保護（白抜きや黒塗りを防ぐ） */
    .stButton button p, .stLinkButton a span {{
        color: inherit !important;
    }}

    /* 4. リンクボタンのスタイルを少し強調して見やすく */
    .stLinkButton a {{
        background-color: #f8f9fa !important;
        border: 1px solid #dee2e6 !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- コンテンツ ---
st.title("🇧🇷 サバンナ八木 応援ポータル")

# --- テレビ情報 ---
st.subheader("🗓️ 最新のテレビ出演情報")
st.link_button(
    "👉 番組表を別タブで開く", 
    "https://bangumi.org/talents/142568",
    type="primary",
    use_container_width=True
)

st.divider()

# --- stand.fm ---
st.subheader("💰 stand.fm「お金のしゃべり場」")
st.components.v1.iframe("https://stand.fm/embed/channels/674833f669bc2015d09df281", height=450)

st.link_button(
    "📻 stand.fm 公式サイトを別タブで開く", 
    "https://stand.fm/channels/674833f669bc2015d09df281",
    use_container_width=True
)

st.divider()

# --- セクション3：YouTube ---
st.subheader("🎙️ YouTube「芸人男塾」")

# 動画埋め込み
st.video("https://www.youtube.com/watch?v=q10EVteYbgw")

# 【ここを修正】教えていただいた確実なURLに差し替え
st.link_button(
    "🏮 YouTube チャンネルを別タブで開く", 
    "https://www.youtube.com/channel/UCYhNHFMZZ7gGal-RLCm_65Q", 
    use_container_width=True
)

st.divider()

# --- ブラジルボタン ---
if st.button("ブラジルの人、聞こえますかー！"):
    st.balloons()
    st.success("「聞こえたよー！」（ブラジルの裏側より）")
