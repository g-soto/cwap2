from config import config


class CWPerformer:

    CW_BOT = config.channels.CW

    def __init__(self, post_message, **_) -> None:
        self.post_message = post_message
        self.subs = [("request_weather", self.request_weather)]

    async def request_weather(self, *_):
        await self.post_message(self.CW_BOT, "/time")
