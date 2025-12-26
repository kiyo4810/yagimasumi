import streamlit as st

# サイトの基本設定
st.set_page_config(page_title="サバンナ八木 応援ポータル", page_icon="📺")

# --- タイトル ---
st.title("📺 サバンナ八木真澄 応援ポータル")

# --- セクション1：最新のテレビ出演情報 ---
st.subheader("🗓️ 最新のテレビ出演情報")
st.link_button(
    "👉 八木さんの最新番組表を開く（bangumi.org）", 
    "https://bangumi.org/talents/142568",
    type="primary"
)

st.divider()

# --- セクション2：stand.fm「お金のしゃべり場」 ---
st.subheader("💰 stand.fm「お金のしゃべり場」")
st.write("FP1級の八木塾長が「お金」についておしゃべり！")

# 【ここが重要！】チャンネル全体の埋め込みプレイヤー
# これなら更新作業なしで、常に最新の放送が一番上に表示されます。
st.components.v1.iframe("https://stand.fm/embed/channels/674833f669bc2015d09df281", height=450)

st.link_button("📻 すべての過去放送を聴く", "https://stand.fm/channels/674833f669bc2015d09df281")

st.divider()

# --- セクション3：YouTube「芸人男塾」 ---
st.subheader("🎙️ YouTube「芸人男塾」")
# 2025年M-1結果回
latest_video_id = "q10EVteYbgw" 
st.video(f"https://www.youtube.com/watch?v={latest_video_id}")
st.link_button("🏮「芸人男塾」TOPへ", "https://www.youtube.com/@yagiotokojuku")

st.divider()

# --- お約束のボタン ---
if st.button("ブラジルの人、聞こえますかー！"):
    st.balloons()
    st.success("「聞こえたよー！」（ブラジルの裏側より）")
