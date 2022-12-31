class CraftPerformer:

    GURU_CHANNEL = "https://t.me/roadtoguru"

    def __init__(self, post_message_with_author: callable, post_and_pin_message_with_author: callable) -> None:
        self.post_message = post_message_with_author
        self.pin_message = post_and_pin_message_with_author

    async def new_craft(self, message):
        await self.post_message(self.GURU_CHANNEL, message)

    async def new_weather_report(self, message):
        if await self.is_new_weather(message):
            await self.pin_message(self.GURU_CHANNEL, message)

    async def is_new_weather(self, message):
        return True