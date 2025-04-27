"""
２次関数リアルタイム可視化ツール
"""
import streamlit as st
import numpy as np
from common.ui import inject_global_css, render_navbar, render_footer_ad, render_copyright
from realtime_slider import realtime_slider

# ---------- 1) ページ設定 & 共通 UI ----------
st.set_page_config(page_title="２次関数ビジュアライザ | VisualStudyMath", layout="wide")
inject_global_css()
render_navbar(active="math1")
render_footer_ad(
    img_url="https://placehold.co/468x60?text=Ad+Sample",
    link="https://example.com"
)
render_copyright()

# ---------- 2) 数式タイトル ----------
st.markdown(
    """
    <div style="text-align: right; margin: 20px 0;">
        <span style="font-size: 2em;">
    """, 
    unsafe_allow_html=True
)
st.latex(r"\Large y = ax^2 + bx + c")
st.markdown("</span></div>", unsafe_allow_html=True)

# ---------- 3) メインコンテンツ ----------
left, right = st.columns([1.2, 1])

with left:
    vals = realtime_slider(
        a_init=1.0, b_init=0.0, c_init=0.0,
        xmin=-10, xmax=10, ymin=-100, ymax=100,
        key="quad_vis"
    )
if vals is None:
    vals = {"a": 1.0, "b": 0.0, "c": 0.0}
a, b, c = vals["a"], vals["b"], vals["c"]

# ---------- 4) 数式表示 ----------
with right:
    st.subheader("現在の式 (標準形)")

    def term(v, sym, pw=""):
        s = "+" if v >= 0 else "-"
        return f" {s} {abs(v):.1f}{sym}{pw}"

    st.latex(f"y ={term(a,'x','^2')}{term(b,'x')}{term(c,'')}".replace("+ -", "- "))

    # --- 平方完成 ---
    st.markdown("---")
    st.subheader("平方完成")

    if abs(a) > 1e-10:
        p = -b / (2 * a)
        q = a * p**2 + b * p + c
        sq = f"y = {a:.1f}\\left(x {'-' if p >= 0 else '+'} {abs(p):.1f}\\right)^2 " \
             f"{'+' if q >= 0 else '-'} {abs(q):.1f}"
        st.latex(sq)
    else:
        st.latex(f"y = {b:.1f}x {'+' if c >= 0 else '-'} {abs(c):.1f}")

    # --- 因数分解 ---
    st.markdown("---")
    st.subheader("因数分解")

    if abs(a) < 1e-10:
        if abs(b) < 1e-10:
            st.latex(f"y = {c:.1f}")
        else:
            x0 = -c / b
            st.latex(f"y = {b:.1f}\\left(x {'-' if x0 >= 0 else '+'} {abs(x0):.1f}\\right)")
    else:
        D = b**2 - 4 * a * c
        if abs(D) < 1e-10:
            x0 = -b / (2 * a)
            st.latex(f"y = {a:.1f}\\left(x {'-' if x0 >= 0 else '+'} {abs(x0):.1f}\\right)^2")
        elif D > 0:
            x1 = (-b + np.sqrt(D)) / (2 * a)
            x2 = (-b - np.sqrt(D)) / (2 * a)
            fact = f"y = {a:.1f}\\left(x {'-' if x1 >= 0 else '+'} {abs(x1):.1f}\\right)" \
                   f"\\left(x {'-' if x2 >= 0 else '+'} {abs(x2):.1f}\\right)"
            st.latex(fact)
        else:
            st.write("実数解なし（因数分解不可）")