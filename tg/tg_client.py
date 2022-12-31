import yaml
from telethon import TelegramClient

class TGClient:
    def __init__(self) -> None:
        api_config = self.__load_api_config()
        self.client = TelegramClient(session='cw', api_id=api_config["id"], api_hash=api_config["hash"], connection_retries=None)


    def __load_api_config(self):
        with open("config.yml", "rt") as yml_file:
            return yaml.load(yml_file, yaml.SafeLoader)["Telegram API"]

    async def new_chat_event(self):
        pass

    def add_watcher(self, ChatWatcher):
        w = ChatWatcher(self.new_chat_event)
        for watch in w.watchs:
            self.client.add_event_handler(watch)
