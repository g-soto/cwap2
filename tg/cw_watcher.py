import regex as re
from telethon import events

from config import config

weather_re = re.compile(
    "In Chat Wars world now\n"
    "\\W+\\w+\n"
    "[0-9:]+\\n"
    "\\d+ \\w+ \\d+\n"
    "\n"
    "Weather forecast\n"
    "(.+)→(.+)\n"
)


class CWWatcher:

    CW_BOT = config.channels.CW

    def __init__(self, inform_event: callable) -> None:
        self.inform_event = inform_event
        self.watchs = [
            self.watch_for_craft,
            self.watch_for_time,
            self.watch_for_messages
        ]
        self.last_weather = None

    @events.register(events.NewMessage(outgoing=False, chats=CW_BOT))
    async def watch_for_craft(self, event):
        if self.is_craft_message(event):
            await self.inform_event("new_craft", event.message)

    def is_craft_message(self, message):
        return "has ordered" in message.raw_text

    @events.register(events.NewMessage(outgoing=False, chats=CW_BOT))
    async def watch_for_time(self, event):
        if self.is_new_weather_message(event):
            await self.inform_event("new_weather", event.message)

    def is_new_weather_message(self, message):
        if not (m := re.match(weather_re, message.raw_text)):
            return False
        new_weather = m.groups()
        if new_weather == self.last_weather:
            return False
        self.last_weather = new_weather
        return True

    @events.register(events.NewMessage(outgoing=False, chats=CW_BOT))
    async def watch_for_messages(self, event):
        await self.inform_event("new_cw_message", event.message)
