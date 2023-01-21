from config import config


class CraftPerformer:

    GURU_CHANNEL = config.channels.GURU

    def __init__(
        self,
        post_message_with_author: callable,
        post_and_pin_message_with_author: callable,
        **_
    ) -> None:
        self.post_message = post_message_with_author
        self.pin_message = post_and_pin_message_with_author
        self.subs = [
            ("new_craft", self.new_craft),
            ("new_weather", self.new_weather_report),
        ]

    async def new_craft(self, message):
        await self.post_message(self.GURU_CHANNEL, message)

    async def new_weather_report(self, message):
        await self.pin_message(self.GURU_CHANNEL, message)
