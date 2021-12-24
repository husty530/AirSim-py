# AirSim-py

[AirSim](https://microsoft.github.io/AirSim/)はMicrosoftがフリーで公開している自動運転シミュレータです。  
このリポジトリではPythonから操作をするための最低限の手順とサンプルをまとめました。特別な開発環境は必要ありません。  

## Usage

### AirSim側

1. まずは[ダウンロードページ](https://github.com/Microsoft/AirSim/releases)に行って、Assetsからzipファイルを選びます。
(これらの違いはロケーションとファイルサイズだけです。ピンとくるものを選びましょう。)

2. zipを展開したら、開いてすぐのところにある(ナントカ.exe)を開きましょう。うまくいけばこれでAirSim側は完了。
DirectXに関するエラーが出る場合は[DirectX エンドユーザーランタイムを手動でインストールする方法](https://faq.tsukumo.co.jp/index.php?solution_id=1321)
を実行すれば大丈夫なはずです。

3. いちいち車かドローンかを選ばせるダイアログが出てうざいので、本リポジトリに付属している[settings.json](/settings.json)を(ナントカ.exe)と同じ階層に配置します。
これで車をデフォルトにできるほか、GPSやIMU、カメラなどの車載センサも設定できます。詳しくは[setting.jsonの書き方](https://microsoft.github.io/AirSim/settings/)をご覧ください。

### Python側

1. Python自体はインストールされているものとします。以下のコマンドでパッケージを入れます。
```
pip install msgpack-rpc-python
pip install airsim
pip install pynput
```

2. 先にAirSimのexeを起動してから、PowerShellなどでsample.pyのあるディレクトリから以下のコマンドを打つと起動します。
```
python sample.py
```

3. コンソール画面で十字キーで車両の操作、ESCで終了としています。もっといろんなこともできますので、
[Python APIリファレンス](https://microsoft.github.io/AirSim/api_docs/html/)を参考に機能を拡張してみてください。
