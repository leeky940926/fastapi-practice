import os

from slack_sdk import WebClient


def send_slack_message(channel: str, text: str):
    slack_token = os.environ.get("SLACK_TOKEN")
    client = WebClient(token=slack_token)

    return client.chat_postMessage(channel="C04B929S2GP", text="안녕")
