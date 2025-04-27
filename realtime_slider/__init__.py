import os
from typing import Optional
import streamlit.components.v1 as components

# フロントエンドのビルドディレクトリを取得
COMPONENT_DIR = os.path.join(os.path.dirname(__file__), "frontend/dist")

# コンポーネントを登録
_component_func = components.declare_component(
    "realtime_slider",
    path=COMPONENT_DIR
)

def realtime_slider(
    a_init: float = 1.0,
    b_init: float = 0.0,
    c_init: float = 0.0,
    xmin: float = -10,
    xmax: float = 10,
    ymin: float = -100,
    ymax: float = 100,
    key: Optional[str] = None,
) -> dict:
    """
    リアルタイム2次関数ビジュアライザー
    """
    component_value = _component_func(
        a_init=a_init,
        b_init=b_init,
        c_init=c_init,
        xmin=xmin,
        xmax=xmax,
        ymin=ymin,
        ymax=ymax,
        key=key,
        default={"a": a_init, "b": b_init, "c": c_init}
    )
    
    return component_value

__all__ = ['realtime_slider']
