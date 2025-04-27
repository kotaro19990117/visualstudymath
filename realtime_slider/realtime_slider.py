import streamlit as st
import numpy as np
import plotly.graph_objects as go

def realtime_slider(
    a_init: float = 1.0,
    b_init: float = 0.0,
    c_init: float = 0.0,
    xmin: float = -10,
    xmax: float = 10,
    ymin: float = -10,
    ymax: float = 10,
    key: str = None
) -> dict:
    """
    ２次関数のパラメータをリアルタイムに調整するスライダー群
    """
    # スライダー
    a = st.slider("a", -5.0, 5.0, a_init, 0.1, key=f"{key}_a")
    b = st.slider("b", -10.0, 10.0, b_init, 0.1, key=f"{key}_b")
    c = st.slider("c", -10.0, 10.0, c_init, 0.1, key=f"{key}_c")

    # グラフ描画
    x = np.linspace(xmin, xmax, 200)
    y = a * x**2 + b * x + c

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='y'))
    
    # 軸設定
    fig.update_layout(
        xaxis=dict(
            range=[xmin, xmax],
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='#666',
            showgrid=True,
            gridwidth=1,
            gridcolor='#ccc',
        ),
        yaxis=dict(
            range=[ymin, ymax],
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='#666',
            showgrid=True,
            gridwidth=1,
            gridcolor='#ccc',
        ),
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor='white',
    )

    # プロット表示
    st.plotly_chart(fig, use_container_width=True)

    return {"a": a, "b": b, "c": c} 