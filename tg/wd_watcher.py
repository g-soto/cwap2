from telethon import events

from config import config


class WDWatcher:

    WD_CHANNEL = config.channels.WD

    def __init__(self, inform_event: callable) -> None:
        self.inform_event = inform_event
        self.watchs = [self.watch_for_command]

    @events.register(events.NewMessage(chats=WD_CHANNEL))
    async def watch_for_command(self, event):
        if self.is_command_message(event):
            await self.inform_event("new_command", event.message)

    def is_command_message(self, message):
        return message.raw_text.startswith("/cw ")
