from config import config


class CWPerformer:

    CW_BOT = config.channels.CW

    def __init__(self, post_message, **_) -> None:
        self.post_message = post_message
        self.subs = [
            ("request_weather", self.request_weather),
            ("new_command", self.new_cw_command)
            ]

    async def request_weather(self, *_):
        await self.post_message(self.CW_BOT, "/time")

    async def new_cw_command(self, message):
        coomand = message.raw_text[3:]
        await self.post_message(self.CW_BOT, coomand)
