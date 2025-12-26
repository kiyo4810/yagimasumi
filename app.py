import streamlit as st

st.set_page_config(page_title="サバンナ八木 応援ポータル", page_icon="🇧🇷")

# --- 背景画像の設定 ---
yagi_url = "https://raw.githubusercontent.com/kiyo4810/yagimasumi/main/images/yagi_bg.jpg"

# --- 【完全版】スタイル設定（背景1枚固定 ＆ ダークモード・エラー対策） ---
st.markdown(
    f"""
    <style>
    /* 1. 背景の設定：リピートを完全に禁止し、1枚を画面中央に固定 */
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)), 
                          url("{yagi_url}");
        background-repeat: no-repeat !important; /* 絶対に繰り返さない */
        background-size: cover !important;    /* 画面全体を覆う */
        background-position: center !important; /* 中央に配置 */
        background-attachment: fixed !important; /* スクロールしても固定 */
    }}

    /* 2. 基本の文字色：ダークモードでも読みやすく黒系に固定 */
    .stApp * {{
        color: #333333 !important;
    }}

    /* 3. ボタンとリンクの調整（文字が消えるのを防ぎ、背景を整える） */
    .stButton button p, .stLinkButton a span {{
        color: inherit !important;
    }}
    
    .stLinkButton a {{
        background-color: #f0f2f6 !important;
        border: 1px solid #d1d5db !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- タイトル ---
st.title("🇧🇷 サバンナ八木 応援ポータル")

# --- セクション1：テレビ出演情報 ---
st.subheader("🗓️ 最新のテレビ出演情報")
st.link_button(
    "👉 番組表を別タブで開く", 
    "https://bangumi.org/talents/142568",
    type="primary",
    use_container_width=True
)

st.divider()

# --- セクション2：stand.fm ---
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

# 動画の埋め込み
st.video("https://www.youtube.com/watch?v=q10EVteYbgw")

# 【重要】YouTubeリンクの修正：チャンネルID形式に変更してエラーを回避
st.link_button(
    "🏮 YouTube チャンネルを別タブで開く", 
    "https://www.youtube.com/channel/UCixVg1_EWdG5pf0ok4OuELA", 
    use_container_width=True
)

st.divider()

# --- お約束のボタン ---
if st.button("ブラジルの人、聞こえますかー！"):
    st.balloons()
    st.success("「聞こえたよー！」（ブラジルの裏側より）")
