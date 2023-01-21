import asyncio as aio
from collections import defaultdict

from telethon import TelegramClient

from config import config


class TGClient:
    def __init__(self) -> None:
        self.client = TelegramClient(
            session="cw",
            api_id=config.telegram_api.ID,
            api_hash=config.telegram_api.HASH,
            connection_retries=None,
        )

        self.subscriptions = defaultdict(list)
        self.performer_methods = {
            val.__name__: val
            for val in (
                self.post_message,
                self.post_message_with_author,
                self.post_and_pin_message_with_author,
            )
        }
        self.scheduled = [self.client.run_until_disconnected]

    async def start(self):
        await self.client.start()
        return await aio.wait([
            aio.create_task(sch()) for sch in self.scheduled
            ])

    async def stop(self):
        return await self.client.disconnect()

    async def new_chat_event(self, source, event):
        await aio.wait([
            aio.create_task(sub(event)) for sub in self.subscriptions[source]
            ])

    async def post_message(self, chat, message):
        return await self.client.send_message(chat, message)

    async def post_message_with_author(self, chat, message):
        return await self.client.forward_messages(chat, message)

    async def post_and_pin_message_with_author(self, chat, message):
        await self.client.pin_message(
            chat, await self.post_message_with_author(chat, message)
        )

    def add_watcher(self, ChatWatcher):
        for watch in ChatWatcher(self.new_chat_event).watchs:
            self.client.add_event_handler(watch)

    def add_performer(self, ChatPerformer):
        for source, performer in ChatPerformer(**self.performer_methods).subs:
            self.subscriptions[source].append(performer)

    def add_scheduler(self, EventScheduler):
        self.scheduled += EventScheduler(
            self.new_chat_event, self.client.is_connected
        ).scheduled
