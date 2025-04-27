"""
数学Ⅰトップページ（分野別ツール一覧）
"""
import streamlit as st
from common.ui import (
    inject_global_css, render_navbar,
    render_footer_ad,  render_copyright
)

st.set_page_config(page_title="数学Ⅰ | VisualStudyMath", layout="wide")

# ---------- 共通 UI ----------
inject_global_css()
render_navbar(active="math1")
render_footer_ad(
    img_url="https://placehold.co/468x60?text=Ad+Sample",
    link="https://example.com"
)
render_copyright()

# ---------- コンテンツ ----------
st.header("数学Ⅰ｜分野別ツール一覧")
st.info("このページは現在準備中です。もう少しお待ちください！")

# ▼ 例：ツールを追加するとき ------------------
# col1, col2 = st.columns(2)
# with col1:
#     st.subheader("2次関数ビジュアライザ")
#     st.page_link("app.py", label="▶ 開く")  # 別ページへリンク
# --------------------------------------------- 