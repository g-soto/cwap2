import asyncio as aio

class CWScheduler:
    def __init__(self, inform_event, is_connected) -> None:
        self.inform_event = inform_event
        self.is_connected = is_connected
        self.scheduled = [self.time_requester]

    async def time_requester(self):
        waiting_time = 30*60
        while self.is_connected():
            await self.inform_event("request_weather", None)
            await aio.sleep(waiting_time)