import yaml
from telethon import TelegramClient
import asyncio as aio
from collections import defaultdict

class TGClient:
    def __init__(self) -> None:
        api_config = self.__load_api_config()
        self.client = TelegramClient(session='cw', api_id=api_config["id"], api_hash=api_config["hash"], connection_retries=None)
        self.subscriptions = defaultdict(list)
        self.performer_methods = {val.__name__: val for val in (self.post_message, self.post_message_with_author, self.post_and_pin_message_with_author)}


    async def start(self):
        await self.client.start()
        return await self.client.run_until_disconnected()

    async def stop(self):
        return await self.client.disconnect()

    def __load_api_config(self):
        with open("config.yml", "rt") as yml_file:
            return yaml.load(yml_file, yaml.SafeLoader)["Telegram API"]

    async def new_chat_event(self, source, event):
        await aio.wait([aio.create_task(sub(event)) for sub in self.subscriptions[source]])

    async def post_message(self, chat, message):
        return await self.client.send_message(chat, message)

    async def post_message_with_author(self, chat, message):
        return await self.client.forward_messages(chat, message)

    async def post_and_pin_message_with_author(self, chat, message):
        await self.client.pin_message(chat, await self.post_message_with_author(chat, message))

    def add_watcher(self, ChatWatcher):
        w = ChatWatcher(self.new_chat_event)
        for watch in w.watchs:
            self.client.add_event_handler(watch)

    def add_performer(self, ChatPerformer):
        p = ChatPerformer(**self.performer_methods)
        for source, performer in p.subs:
            self.subscriptions[source].append(performer)
