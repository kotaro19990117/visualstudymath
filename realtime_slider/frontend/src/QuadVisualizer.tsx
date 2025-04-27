import React, { useEffect, useRef, useState } from 'react'
import { Streamlit, ComponentProps } from 'streamlit-component-lib'
import Plotly from 'plotly.js-dist-min'

// 型定義を修正
interface PythonArgs {
  a_init: number
  b_init: number
  c_init: number
  xmin: number
  xmax: number
  ymin: number
  ymax: number
}

const QuadVisualizer: React.FC<ComponentProps> = (props) => {
  // 引数の取得方法を修正
  const args = props.args as PythonArgs
  const {
    a_init = 1.0,
    b_init = 0.0,
    c_init = 0.0,
    xmin = -10,
    xmax = 10,
    ymin = -100,
    ymax = 100
  } = args || {}  // デフォルト値を設定

  const [a, setA] = useState(a_init)
  const [b, setB] = useState(b_init)
  const [c, setC] = useState(c_init)
  const plotRef = useRef<HTMLDivElement>(null)

  // グラフ更新関数
  const updatePlot = () => {
    if (!plotRef.current) return

    const x = new Array(200).fill(0).map(
      (_, i) => xmin + (i * (xmax - xmin)) / 199
    )
    const y = x.map(xi => a * xi * xi + b * xi + c)

    const trace = {
      x,
      y,
      mode: 'lines',
      line: { color: '#1f77b4', width: 2 }
    }

    const layout = {
      xaxis: {
        range: [xmin, xmax],
        zeroline: true,
        zerolinewidth: 2,
        zerolinecolor: '#666',
        showgrid: true,
        gridwidth: 1,
        gridcolor: '#ccc'
      },
      yaxis: {
        range: [ymin, ymax],
        zeroline: true,
        zerolinewidth: 2,
        zerolinecolor: '#666',
        showgrid: true,
        gridwidth: 1,
        gridcolor: '#ccc'
      },
      margin: { l: 40, r: 40, t: 10, b: 40 },
      showlegend: false,
      plot_bgcolor: 'white'
    }

    Plotly.newPlot(plotRef.current, [trace], layout, { responsive: true })
  }

  // 値が変更されたらStreamlitに通知
  useEffect(() => {
    Streamlit.setComponentValue({ a, b, c })
    updatePlot()
  }, [a, b, c])

  // コンポーネントのサイズが変更されたら再描画
  useEffect(() => {
    const resizeObserver = new ResizeObserver(updatePlot)
    if (plotRef.current) {
      resizeObserver.observe(plotRef.current)
    }
    return () => resizeObserver.disconnect()
  }, [])

  // コンポーネントの準備ができたことを通知
  useEffect(() => {
    Streamlit.setFrameHeight()
  }, [])

  return (
    <div style={{ padding: '1rem', width: '100%' }}>
      <div style={{ marginBottom: '1rem' }}>
        <label style={{ display: 'block', marginBottom: '0.5rem' }}>
          a: {a.toFixed(2)}
        </label>
        <input
          type="range"
          min="-5"
          max="5"
          step="0.01"
          value={a}
          onChange={e => setA(parseFloat(e.target.value))}
          style={{ width: '100%' }}
        />
      </div>
      
      <div style={{ marginBottom: '1rem' }}>
        <label style={{ display: 'block', marginBottom: '0.5rem' }}>
          b: {b.toFixed(2)}
        </label>
        <input
          type="range"
          min="-10"
          max="10"
          step="0.01"
          value={b}
          onChange={e => setB(parseFloat(e.target.value))}
          style={{ width: '100%' }}
        />
      </div>

      <div style={{ marginBottom: '1rem' }}>
        <label style={{ display: 'block', marginBottom: '0.5rem' }}>
          c: {c.toFixed(2)}
        </label>
        <input
          type="range"
          min="-10"
          max="10"
          step="0.01"
          value={c}
          onChange={e => setC(parseFloat(e.target.value))}
          style={{ width: '100%' }}
        />
      </div>

      <div ref={plotRef} style={{ width: '100%', height: '400px' }} />
    </div>
  )
}

export default QuadVisualizer 