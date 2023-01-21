from .craft_performer import CraftPerformer
from .cw_performer import CWPerformer
from .cw_scheduler import CWScheduler
from .cw_watcher import CWWatcher
from .tg_client import TGClient
from .wd_performer import WDPerformer
from .wd_watcher import WDWatcher


def create_client():
    tgc = TGClient()
    tgc.add_watcher(CWWatcher)
    tgc.add_watcher(WDWatcher)

    tgc.add_performer(CraftPerformer)
    tgc.add_performer(CWPerformer)
    tgc.add_performer(WDPerformer)

    tgc.add_scheduler(CWScheduler)

    return tgc
