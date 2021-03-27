## 情報基礎 ミニプロジェクト
慶應義塾大学　情報基礎2　ミニプロジェクト

## 必要モジュール
pyxel: v1.4.3

詳しくは、「requirements.txt」をご参照ください。

### ゲームルール
画面上にピンク色の球ときいろの球が出現します。
マウスを用いて、球をクリックするとポイントが入ります。
さらにマウスが、球の中心点に近づけば近づくほど得点は高くなります。ちなみに、外周付近と中心座標では、最大10倍のポイント差があります

### store.log
このファイルは、あなたのプレイスコアを永続的に保持する目的で使用されます。
このファイルを削除することによって、あたたのスコアは全て初期化されます。
また、このファイルは初回起動時に自動生成されます。

store.logファイルには、デフォルトでサンプルの値が含まれています。

### 実行方法

```python3 -m app.py``` with pyenv (any virtual python environment)
