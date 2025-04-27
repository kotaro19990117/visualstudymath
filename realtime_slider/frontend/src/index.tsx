import React from "react"
import { createRoot } from "react-dom/client"
import { ComponentProps, withStreamlitConnection } from "streamlit-component-lib"
import QuadVisualizer from "./QuadVisualizer"

// React 18 の createRoot を使用
const root = createRoot(document.getElementById("root")!)

// StreamlitProvider の代わりに withStreamlitConnection を使用
const ConnectedQuadVisualizer = withStreamlitConnection(QuadVisualizer)

root.render(
  <React.StrictMode>
    <ConnectedQuadVisualizer />
  </React.StrictMode>
) 