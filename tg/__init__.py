from .tg_client import TGClient
from .cw_watcher import CWWatcher

def create_client():
    tgc = TGClient()
    tgc.add_watcher(CWWatcher)