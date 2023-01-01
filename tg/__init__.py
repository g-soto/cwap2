from .tg_client import TGClient
from .cw_watcher import CWWatcher
from .craft_performer import CraftPerformer
from .cw_performer import CWPerformer
from .cw_scheduler import CWScheduler

def create_client():
    tgc = TGClient()
    tgc.add_watcher(CWWatcher)
    tgc.add_performer(CraftPerformer)
    tgc.add_performer(CWPerformer)
    tgc.add_scheduler(CWScheduler)
    return tgc