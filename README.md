# operate-slack

## 必須モジュール

- slack提供のSDK

``` txt
slack_sdk
```

## 機能概要

- 「create_channels_info.json」の情報をもとにSlackチャンネルを作成
  - 説明も追加
  - 初期メンバーの追加は後日
- 実行結果は「logs」フォルダにログファイルを出力

## 環境変数について

- 「.env」ファイルをpythonファイルと同一の階層に作成し、変数を定義することでスクリプト内で参照可能
