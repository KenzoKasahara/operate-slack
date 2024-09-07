# operate-slack

## 必須モジュール

- slack提供のSDK

``` txt
slack_sdk
```

## Slackでアプリ作成時に付与必須権限

- 事前にSlackアプリを作成する必要あり
- 作成後、「Outh Tokens」を発行し、環境変数に保存
- 「Scopes」にて以下の権限を付与する
  - Outh & Permissions
  - channels:manage
  - groups:write
  - im:write
  - mpim:write

## 機能概要

- 「create_channels_info.json」の情報をもとにSlackチャンネルを作成
  - 説明も追加
  - 初期メンバーの追加は後日
- 実行結果は「logs」フォルダにログファイルを出力

## 環境変数について

- 「.env」ファイルをpythonファイルと同一の階層に作成し、変数を定義することでスクリプト内で参照可能
