import streamlit as st
import feedparser

# サイトの基本設定
st.set_page_config(page_title="サバンナ八木 応援ポータル", page_icon="📺")

# --- stand.fmの最新情報を取得する関数 ---
@st.cache_data(ttl=3600)  # 1時間キャッシュ
def get_standfm_latest():
    # stand.fmの公式RSSフィードURL
    rss_url = "https://stand.fm/rss/channels/674833f669bc2015d09df281"
    try:
        feed = feedparser.parse(rss_url)
        return feed.entries
    except:
        return []

# --- タイトル ---
st.title("📺 サバンナ八木真澄 応援ポータル")

# --- セクション1：テレビ出演情報 ---
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

entries = get_standfm_latest()

if entries:
    # 最新回を取得
    latest_ep = entries[0]
    # URLからエピソードIDを抽出 (https://stand.fm/episodes/xxxxx -> xxxxx)
    latest_id = latest_ep.link.split('/')[-1]
    
    # 1. 最新回の埋め込みプレイヤー
    st.components.v1.iframe(f"https://stand.fm/embed/episodes/{latest_id}", height=160)
    
    # 2. メインリンク
    st.link_button("📻 番組TOPページ（stand.fm）", "https://stand.fm/channels/674833f669bc2015d09df281")

    # 3. 直近5話へのリンク
    st.markdown("#### 📚 最近の配信アーカイブ")
    for entry in entries[:5]:
        st.markdown(f"・[{entry.title}]({entry.link})")
else:
    st.warning("ラジオの最新情報を読み込み中です。直接サイトをご確認ください。")
    st.link_button("📻 stand.fm チャンネルへ", "https://stand.fm/channels/674833f669bc2015d09df281")

st.divider()

# --- セクション3：YouTube「芸人男塾」 ---
st.subheader("🎙️ YouTube「芸人男塾」")
latest_video_id = "q10EVteYbgw" 
st.video(f"https://www.youtube.com/watch?v={latest_video_id}")
st.link_button("🏮「芸人男塾」TOPへ", "https://www.youtube.com/@yagiotokojuku")

st.divider()

if st.button("ブラジルの人、聞こえますかー！"):
    st.balloons()
    st.success("「聞こえたよー！」（ブラジルの裏側より）")
