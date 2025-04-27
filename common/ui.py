"""
共通 UI（CSS, ヘッダー, フッター, コピーライト）
"""
import streamlit as st

# ---------- ① CSS 注入（１回だけ呼ぶ） ----------
def inject_global_css() -> None:
    st.markdown(
        """
        <style>
        /* ここに前回提示の CSS をそのまま貼り付け */
        /* --- 現在ページをハイライト --- */
        .nav-link.nav-active {
            opacity: 1 !important;
            border-bottom: 3px solid #fff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# ---------- ② ヘッダー ----------
def render_navbar(active: str = "top") -> None:
    """
    active : 今いるページ（top / math1 / math2 ...）
    """
    menu = [
        ("Home",   "/",      "top"),
        ("数学Ⅰ", "/math1", "math1"),
        ("数学Ⅱ", "/math2", "math2"),
        ("数学Ⅲ", "/math3", "math3"),
        ("数学A", "/matha", "matha"),
        ("数学B", "/mathb", "mathb"),
        ("数学C", "/mathc", "mathc"),
    ]
    links = "".join(
        f'<a href="{url}" class="nav-link{" nav-active" if key==active else ""}">{name}</a>'
        for name, url, key in menu
    )
    st.markdown(
        f"""
        <header class="nav-header">
            <span class="nav-title">数学教材素材</span>
            <nav class="nav-menu">{links}</nav>
        </header>
        """,
        unsafe_allow_html=True
    )

# ---------- ③ フッター広告 ----------
def render_footer_ad(img_url: str, link: str = "#"):
    st.markdown(
        f"""
        <div class="ad-footer">
            <a href="{link}" target="_blank" rel="noopener">
                <img src="{img_url}" alt="footer banner">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- ④ コピーライト ----------
def render_copyright(text: str = "© 2025 kotaro19990117"):
    st.markdown(f'<div class="copyright-bar">{text}</div>', unsafe_allow_html=True) 