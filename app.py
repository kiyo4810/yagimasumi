import streamlit as st

st.set_page_config(page_title="サバンナ八木 応援ポータル", page_icon="🇧🇷")

# --- 画像URLの設定 ---
yagi_url = "https://raw.githubusercontent.com/kiyo4810/yagimasumi/main/images/yagi_bg.jpg"

# --- スタイル設定（背景1枚固定 ＆ ダークモード対策） ---
st.markdown(
    f"""
    <style>
    /* 1. 背景の設定：リピートを完全に禁止し、1枚を中央に固定 */
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)), 
                          url("{yagi_url}");
        background-repeat: no-repeat !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* 2. 基本の文字色：ダークモードでも読みやすく黒系に固定 */
    .stApp * {{
        color: #333333 !important;
    }}

    /* 3. ボタンとリンクの調整（文字が消えるのを防ぐ） */
    .stButton button p, .stLinkButton a span {{
        color: inherit !important;
    }}

    /* 4. リンクボタン自体の背景を少し見やすくする */
    .stLinkButton a {{
        background-color: rgba(0, 0, 0, 0.05) !important;
        border: 1px solid #cccccc !important;
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

# --- セクション3：YouTube（修正版） ---
st.subheader("🎙️ YouTube「芸人男塾」")

# 動画の埋め込み（これは動作しているはずです）
st.video("https://www.youtube.com/watch?v=q10EVteYbgw")

# 【修正ポイント】YouTubeリンクのエラー対策
# @記号付きのURLでエラーが出る場合、チャンネルのURLをこちらに差し替えてみてください
st.link_button(
    "🏮 YouTube チャンネルを別タブで開く", 
    "https://www.youtube.com/channel/UCy7V7L8hR4l_Xp76D9Wv5qA", # @yagiotokojuku のID版URL
    use_container_width=True
)

st.divider()

# --- お約束のボタン ---
if st.button("ブラジルの人、聞こえますかー！"):
    st.balloons()
    st.success("「聞こえたよー！」（ブラジルの裏側より）")
