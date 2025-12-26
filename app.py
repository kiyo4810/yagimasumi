import streamlit as st

st.set_page_config(page_title="サバンナ八木 応援ポータル", page_icon="🇧🇷")

# --- 背景画像の設定 (CSS) ---
# あなたのGitHubの画像URLを直接指定します
# ※「kiyo4810」の部分がご自身のGitHubユーザー名と一致しているか確認してください
bg_image_url = "https://raw.githubusercontent.com/kiyo4810/yagimasumi-info/main/images/yagi_bg.jpg"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{bg_image_url}");
        background-repeat: repeat;
        background-size: 200px auto;
        background-attachment: fixed;
    }}
    /* 背景を30%の濃さにする（70%の白を被せる） */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255, 255, 255, 0.7);
        z-index: -1;
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
