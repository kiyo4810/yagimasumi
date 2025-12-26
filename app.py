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
    /* 全体の背景を設定 */
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9)), 
                    url("{yagi_url}");
        background-repeat: repeat;
        background-size: 200px auto;
        background-attachment: fixed;
    }}
    
    /* コンテンツを見やすくするために背景を白っぽく透過させる */
    header, .main, .stApp {{
        background-color: rgba(255, 255, 255, 0.3);
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
