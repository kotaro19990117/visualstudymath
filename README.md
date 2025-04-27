📜【VisualStudyMath 作業用コマンドまとめ（完全版・最新版）】

# VisualStudyMath 開発・運用コマンドまとめ

---

## 🔥 仮想環境 (venv) 起動

```bash
source ~/venv/bin/activate
（作業するたびに必ずやる！）


🚀 Streamlit アプリを起動（ポート80）

sudo ~/venv/bin/python3.12 -m streamlit run app.py --server.address=0.0.0.0 --server.port=80
※ポート80は特権ポートなので必ず sudo が必要


🔄 リポジトリを最新に更新 (Git Pull)

git pull
（ローカルをGitHub最新に合わせる）


📦 Reactコンポーネント（frontend）ビルド準備

① 最初のnpm install（1回だけでOK）
cd realtime_slider/frontend
npm install
（Node.jsのライブラリを最初にインストールする）


📦 Reactコンポーネント（frontend）ビルド

② 通常ビルド
NODE_OPTIONS="--max_old_space_size=2048" npm run build
（※サーバーのメモリ制限回避のため NODE_OPTIONS を付ける）


🛠️ ビルド失敗時の対応

（メモリ不足エラーが出た場合）
サーバーにSwap領域を作る（必要なら）
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
そのあと再ビルドする
NODE_OPTIONS="--max_old_space_size=2048" npm run build


📡 サーバーIP・ドメイン状態確認（DNSチェック）

dig visualstudymath.com +short
または
nslookup visualstudymath.com
（Elastic IPが返ってくればOK）


📦 必要なPythonライブラリをインストール

（仮想環境内で）
pip install -r requirements.txt
or 必要に応じて個別インストール
pip install streamlit altair pandas numpy plotly


🚪 仮想環境から抜ける

deactivate


---

## ☀️ バックグラウンドでStreamlitを起動する（本番用）

通常のターミナル起動だとブラウザを閉じると止まってしまうので、  
本番運用時は `nohup` を使ってバックグラウンド起動する！

```bash
nohup sudo ~/venv/bin/python3.12 -m streamlit run app.py --server.address=0.0.0.0 --server.port=80 &
nohup ：ターミナルを閉じてもプロセスが生きる
& ：バックグラウンドで動かす
ログは自動で nohup.out に保存される
📖 バックグラウンドプロセスの管理

ログを見る
cat nohup.out
（リアルタイムログを見たいなら tail -f nohup.out）
プロセスを止める方法
Streamlitのプロセスを探す
ps aux | grep streamlit
プロセスID（PID）をkillする
sudo kill プロセスID
（例：sudo kill 5837）