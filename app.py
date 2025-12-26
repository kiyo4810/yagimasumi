import streamlit as st

st.set_page_config(page_title="サバンナ八木 応援ポータル", page_icon="🇧🇷")

# --- 背景画像の設定 (CSS) ---
# 公開URLやユーザー名に合わせて、GitHub上の画像への「直通リンク」を再設定しました
# images/yagi_bg.jpg が GitHub の images フォルダ内にあることを前提としています
bg_image_url = "https://www.streamlit.io/images/brand/streamlit-mark-color.png"

# --- 背景画像の設定 (最新安定版CSS) ---
# まずはテスト画像で確認。表示されたら以下のURLを八木さんのものに書き換えてください。
test_url = "https://www.streamlit.io/images/brand/streamlit-mark-color.png"
yagi_url = "https://raw.githubusercontent.com/kiyo4810/yagimasumi/main/images/yagi_bg.jpg"

st.markdown(
    f"""
    <style>
    /* 1. 全体の背景設定：リピートを禁止し、1枚を画面いっぱいに表示 */
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)), 
                          url("{yagi_url}");
        background-repeat: no-repeat !important; /* リピートを絶対にさせない */
        background-size: cover !important;    /* 画面全体を覆う */
        background-position: center !important; /* 中央に配置 */
        background-attachment: fixed !important; /* スクロールしても動かさない */
    }}

    /* 2. 文字色対策：背景が白系なので、文字を「濃いグレー」に強制固定 */
    /* ダークモードでも文字が白くならないようにします */
    .stApp * {{
        color: #333333 !important;
    }}

    /* 3. ボタンとリンクの調整 */
    /* ボタンの中身や特定のリンクが黒ずんで見えなくなるのを防ぎます */
    .stButton button p, .stLinkButton a span, .stAlert p {{
        color: inherit !important;
    }}
    
    /* 4. YouTube等の埋め込みエリアの背景を整える */
    iframe {{
        background-color: white;
        border-radius: 10px;
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

st.markdown(
    """
    <a href="https://stand.fm/channels/674833f669bc2015d09df281" target="_blank"
       style="display: inline-block; padding: 10px 20px; background-color: #008080; color: white; 
       text-decoration: none; border-radius: 5px; width: 100%; text-align: center;">
       📻 stand.fm 公式サイトを別タブで開く
    </a>
    """,
    unsafe_allow_html=True
)

st.divider()

# --- セクション3：YouTube ---
st.subheader("🎙️ YouTube「芸人男塾」")
st.video("https://www.youtube.com/watch?v=q10EVteYbgw")

st.link_button(
    "🏮 YouTube を別タブで開く", 
    "https://www.youtube.com/@yagiotokojuku",
    use_container_width=True
)

st.divider()

# --- お約束のボタン ---
if st.button("ブラジルの人、聞こえますかー！"):
    st.balloons()
    st.success("「聞こえたよー！」（ブラジルの裏側より）")
