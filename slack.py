import os
import json

from logging import getLogger, FileHandler, Formatter, DEBUG
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv


load_dotenv()
SLACK_ACCESS_TOKEN = os.environ['SLACK_API_TOKEN']  # OAuth Tokensを設定


# ロギング設定
def my_logging():
    # ロギング設定（親設定）
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)    # [DEBUG: 10, INFO: 20, WARNING: 30, ERROR: 40, CRITICAL: 50]のいずれかを指定
    format = "[%(levelname)-9s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s"

    # 出力先の設定（子設定）
    handler = FileHandler(filename='./logs/operate_slack.log', encoding='utf-8')
    handler.setFormatter(Formatter(format))

    # ロギング設定の適用
    logger.addHandler(handler)
    logger.propagate = False    # 親設定を引き継がない

    return logger


def create_channel(client, channel_name, logger):
    logger.info('Slackチャンネル作成処理開始')
    try:
        response = client.conversations_create(
            name=channel_name
        )
        # チャンネルIDを取得
        channel_id = response['channel']['id']
        logger.info('Slackチャンネルを作成しました: %s', channel_name)
        return channel_id
    except SlackApiError as e:
        logger.error(f"エラーが発生しました: {e.response}")
        raise


def add_discription(client, channel_id, discription, logger):
    logger.info("チャンネルの説明更新処理開始")
    try:
        client.conversations_setPurpose(
            channel=channel_id,
            purpose=discription
        )
        logger.info("チャンネルの説明が更新されました")
    except SlackApiError as e:
        logger.error(f"エラーが発生しました: {e.response['error']}")
        raise


def main():
    logger = my_logging()

    logger.info('【処理開始】')

    # Slack APIトークン (Slack APIから取得したトークンを設定)
    client = WebClient(token=SLACK_ACCESS_TOKEN)
    api_response = client.api_test()
    logger.info(f'疎通テスト: {api_response["ok"]}')

    # チャンネル作成情報の読み込み
    with open('create_channels_info.json', 'r') as f:
        channels_info = json.load(f)

    # チャンネル作成と説明の追加
    for channel_info in channels_info['slack']:
        channel_name = channel_info['channel_name']
        discription = channel_info['discription']

        channel_id = create_channel(client, channel_name, logger)
        add_discription(client, channel_id, discription, logger)

    logger.info('【処理終了】')


if __name__ == '__main__':
    main()
