from telethon import events

class CWWatcher:
    
    CW_BOT = '@chtwrsbot'

    def __init__(self, inform_event: callable) -> None:
        self.inform_event = inform_event
        self.watchs = [self.watch_for_craft, self.watch_for_time]
        
    @events.register(events.NewMessage(outgoing=False, chats=CW_BOT))
    async def watch_for_craft(self, event):
        if self.is_craft_message(event):
            await self.inform_event("new_craft", event.message)

    def is_craft_message(self, message):
        return 'has ordered' in message.raw_text

    @events.register(events.NewMessage(outgoing=False, chats=CW_BOT))
    async def watch_for_time(self, event):
        if "Weather forecast" in event.raw_text:
            await self.inform_event("new_weather", event.message)