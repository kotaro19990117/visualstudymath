"""
トップページ：単元リスト表
"""
import streamlit as st
import pandas as pd
from common.ui import (
    inject_global_css,
    render_navbar,
    render_footer_ad,
    render_copyright
)

# ---------- 0) ページ設定 ----------
st.set_page_config(
    page_title="VisualStudyMath | 単元リスト",
    layout="wide",
)

# ---------- 1) 共通 UI ----------
inject_global_css()
render_navbar(active="top")
render_footer_ad(
    img_url="https://placehold.co/468x60?text=Ad+Sample",
    link="https://example.com"
)
render_copyright()

# ---------- 2) 単元リストデータ ----------
topics = {
    "数学Ⅰ": [
        ("数と式",                None),
        ("２次関数",              "math1_quad_visualizer"),  # パスを変更
        ("三角比",                None),
        ("データの分析",          None),
    ],
    "数学Ⅱ": [
        ("式と計算",              None),
        ("図形と方程式",          None),
        ("指数関数・対数関数",    None),
        ("三角関数",              None),
        ("微分法",                None),
        ("積分法",                None),
    ],
    "数学Ⅲ": [
        ("極限",                  None),
        ("微分法",                None),
        ("積分法",                None),
    ],
    "数学A": [
        ("場合の数",              None),
        ("確率",                  None),
        ("整数",                  None),
        ("図形の性質",            None),
    ],
    "数学B": [
        ("数列",                  None),
        ("ベクトル",              None),
    ],
    "数学C": [
        ("行列",                  None),
        ("ベクトル解析",          None),
        ("複素数平面",            None),
    ],
}

# ---------- 3) DataFrame 生成 ----------
records = []
for subject, units in topics.items():
    for unit, path in units:
        link_text = f"[▶ 開く](/{path})" if path else "準備中"  # スラッシュを先頭に
        records.append({
            "教科": subject,
            "単元": unit,
            "リンク": link_text
        })

df = pd.DataFrame(records)

# ---------- 4) 表示 ----------
st.header("単元リスト（β版）")
st.markdown("""
<div style="
    height: 3px;
    background: linear-gradient(90deg, #ff9c4b, #ff6a8f);
    margin: 10px 0 20px 0;
"></div>
""", unsafe_allow_html=True)

st.markdown(
    "下表の **リンク** をクリックすると対応ツールや解説ページへ遷移します。\
    *準備中* のものは今後順次公開予定です。"
)

# `unsafe_allow_html=True` 付きで Markdown を解釈させる
st.write(
    df.to_markdown(index=False), 
    unsafe_allow_html=True
) 