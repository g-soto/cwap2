import yaml
from telethon import TelegramClient
import asyncio as aio
from collections import defaultdict

class TGClient:
    def __init__(self) -> None:
        api_config = self.__load_api_config()
        self.client = TelegramClient(session='cw', api_id=api_config["id"], api_hash=api_config["hash"], connection_retries=None)
        self.subscriptions = defaultdict(list)


    def __load_api_config(self):
        with open("config.yml", "rt") as yml_file:
            return yaml.load(yml_file, yaml.SafeLoader)["Telegram API"]

    async def new_chat_event(self, source, event):
        await aio.wait(sub(event) for sub in self.subscriptions[source])

    def add_watcher(self, ChatWatcher):
        w = ChatWatcher(self.new_chat_event)
        for watch in w.watchs:
            self.client.add_event_handler(watch)

    def subscribe_performer(self, source, performer):
        self.subscriptions[source].append(performer)

