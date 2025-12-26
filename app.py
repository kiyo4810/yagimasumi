import streamlit as st

# サイトの基本設定
st.set_page_config(page_title="サバンナ八木 応援ポータル", page_icon="📺")

# --- タイトル ---
st.title("📺 サバンナ八木真澄 応援ポータル")

# --- セクション1：最新のテレビ出演情報 ---
st.subheader("🗓️ 最新のテレビ出演情報")
st.write("「bangumi.org」の八木さん専用ページを別タブで開きます。")
# この【ボタン】をクリックしてください
st.link_button(
    "👉 八木さんの最新番組表を開く（別タブで移動）", 
    "https://bangumi.org/talents/142568",
    type="primary",
    use_container_width=True
)

st.divider()

# --- セクション2：stand.fm「お金のしゃべり場」 ---
st.subheader("💰 stand.fm「お金のしゃべり場」")
st.write("FP1級の八木塾長が「お金」についておしゃべり！")

# 埋め込みプレイヤー
st.components.v1.iframe("https://stand.fm/embed/channels/674833f669bc2015d09df281", height=450)

# この【ボタン】をクリックしてください
st.link_button(
    "📻 stand.fm の公式ページへ（別タブで移動）", 
    "https://stand.fm/channels/674833f669bc2015d09df281",
    use_container_width=True
)

st.divider()

# --- セクション3：YouTube「芸人男塾」 ---
st.subheader("🎙️ YouTube「芸人男塾」")
latest_video_id = "q10EVteYbgw" 
st.video(f"https://www.youtube.com/watch?v={latest_video_id}")

# この【ボタン】をクリックしてください
st.link_button(
    "🏮 YouTube「芸人男塾」へ（別タブで移動）", 
    "https://www.youtube.com/@yagiotokojuku",
    use_container_width=True
)

st.divider()

# --- お約束のボタン ---
if st.button("ブラジルの人、聞こえますかー！"):
    st.balloons()
    st.success("「聞こえたよー！」（ブラジルの裏側より）")
