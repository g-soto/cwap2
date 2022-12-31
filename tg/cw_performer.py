class CWPerformer:

    CW_BOT = '@chtwrsbot'

    def __init__(self, post_message) -> None:
        self.post_message = post_message

    async def request_weather(self):
        await self.post_message(self.CW_BOT, "/time")