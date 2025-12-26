import streamlit as st
import requests

# サイトの基本設定
st.set_page_config(page_title="サバンナ八木 応援ポータル", page_icon="📺")

# --- stand.fmのデータを自動取得する関数 ---
@st.cache_data(ttl=3600)  # 1時間ごとに最新情報をチェック
def get_latest_standfm():
    channel_id = "674833f669bc2015d09df281"
    api_url = f"https://stand.fm/api/v1/channels/{channel_id}/episodes?limit=5"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
    except:
        return None
    return None

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

# --- セクション2：stand.fm「お金のしゃべり場」（自動更新版） ---
st.subheader("💰 stand.fm「お金のしゃべり場」")
st.write("FP1級の八木塾長が「お金」についておしゃべり！")

data = get_latest_standfm()

if data and "episodes" in data:
    episodes = data["episodes"]
    latest_ep = episodes[0]
    
    # 1. 最新回の埋め込みプレイヤー
    # APIから取得した最新のIDを使って自動生成
    st.components.v1.iframe(f"https://stand.fm/embed/episodes/{latest_ep['id']}", height=160)
    
    # 2. メインリンク
    st.link_button("📻 番組TOPページ（stand.fm）", "https://stand.fm/channels/674833f669bc2015d09df281")

    # 3. 直近5話へのリンク（自動生成）
    st.markdown("#### 📚 最近の配信アーカイブ")
    for ep in episodes:
        title = ep.get("title", "無題の配信")
        url = f"https://stand.fm/episodes/{ep['id']}"
        st.markdown(f"・[{title}]({url})")
else:
    # データが取れなかった時のバックアップ表示
    st.warning("ラジオの最新情報を読み込み中です。直接サイトをご確認ください。")
    st.link_button("📻 stand.fm チャンネルへ", "https://stand.fm/channels/674833f669bc2015d09df281")

st.divider()

# --- セクション3：YouTube「芸人男塾」 ---
st.subheader("🎙️ YouTube「芸人男塾」")
# YouTubeも自動化可能ですが、まずは確実な最新動画1件を表示
latest_video_id = "q10EVteYbgw" 
st.video(f"https://www.youtube.com/watch?v={latest_video_id}")
st.link_button("🏮「芸人男塾」TOPへ", "https://www.youtube.com/@yagiotokojuku")

st.divider()

# --- お約束のボタン ---
if st.button("ブラジルの人、聞こえますかー！"):
    st.balloons()
    st.success("「聞こえたよー！」（ブラジルの裏側より）")
