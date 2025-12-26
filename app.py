import streamlit as st

st.set_page_config(page_title="サバンナ八木 応援ポータル", page_icon="📺")

# --- タイトル ---
st.title("📺 サバンナ八木 応援ポータル")

# --- セクション1：テレビ出演情報 ---
st.subheader("🗓️ 最新のテレビ出演情報")

# 通常のボタン
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

# HTMLで「新しいタブ」をより強く指示するリンクの作り方
st.markdown(
    """
    <a href="https://stand.fm/channels/674833f669bc2015d09df281" target="_blank" rel="noopener noreferrer" 
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
