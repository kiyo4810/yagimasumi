import streamlit as st

# サイトの基本設定
st.set_page_config(page_title="サバンナ八木 応援ポータル", page_icon="📺")

# --- タイトル ---
st.title("📺 サバンナ八木真澄 応援ポータル")

# --- セクション1：最新のテレビ出演情報 ---
st.subheader("🗓️ 最新のテレビ出演情報")
# このボタンを押すと、bangumi.org が別タブで開きます
st.link_button(
    "👉 八木さんの最新番組表を開く（外部サイト）", 
    "https://bangumi.org/talents/142568",
    type="primary"
)

st.divider()

# --- セクション2：stand.fm「お金のしゃべり場」 ---
st.subheader("💰 stand.fm「お金のしゃべり場」")
st.write("FP1級の八木塾長が「お金」についておしゃべり！")

# チャンネル全体のプレイヤー（更新不要で常に最新が表示されます）
st.components.v1.iframe("https://stand.fm/embed/channels/674833f669bc2015d09df281", height=450)

# このボタンを押すと、stand.fm の公式ページが別タブで開きます
st.link_button("📻 stand.fmで全エピソードを見る", "https://stand.fm/channels/674833f669bc2015d09df281")

st.divider()

# --- セクション3：YouTube「芸人男塾」 ---
st.subheader("🎙️ YouTube「芸人男塾」")
latest_video_id = "q10EVteYbgw" 
st.video(f"https://www.youtube.com/watch?v={latest_video_id}")

# このボタンを押すと、YouTube が別タブで開きます
st.link_button("🏮「芸人男塾」YouTubeへ", "https://www.youtube.com/@yagiotokojuku")

st.divider()

# --- お約束のボタン ---
if st.button("ブラジルの人、聞こえますかー！"):
    st.balloons()
    st.success("「聞こえたよー！」（ブラジルの裏側より）")
