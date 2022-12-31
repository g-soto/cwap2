from telethon import events

class CWWatcher:
    def __init__(self, inform_event: callable) -> None:
        self.inform_event = inform_event
        self.watchs = [self.watch_for_craft]
        
    @events.register(events.NewMessage(outgoing=False))
    async def watch_for_craft(self, event):
        if self.is_craft_message(event):
            await self.inform_event(event.message)

    def is_craft_message(self, message):
        return 'has ordered' in message.raw_text