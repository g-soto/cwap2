from config import config


class WDPerformer:

    WD_CHANNEL = config.channels.WD

    def __init__(self, post_message_with_author: callable, **_) -> None:
        self.post_message = post_message_with_author
        self.subs = [("new_cw_message", self.new_cw_message)]

    async def new_cw_message(self, message):
        await self.post_message(self.WD_CHANNEL, message)
