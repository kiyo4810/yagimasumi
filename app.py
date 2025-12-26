import streamlit as st

# サイトのタイトル
st.set_page_config(page_title="サバンナ八木 出演情報", page_icon="📺")
st.title("📺 サバンナ八木真澄 出演情報")

st.write("自動取得の代わりに、1タップで最新の番組表を開けるようにしました。")

# --- メインボタン ---
# これを押すと、あなたがさっき見ていた「あの画面」が別タブで開きます
st.link_button(
    "👉 八木さんの最新番組表を開く（bangumi.org）", 
    "https://bangumi.org/talents/142568",
    type="primary"
)

st.divider()

# おまけ：八木さんといえば！
if st.button("ブラジルの人、聞こえますかー！"):
    st.balloons()
    st.success("「聞こえたよー！」（ブラジルの裏側より）")
