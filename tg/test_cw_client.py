import asyncio as aio

from tg import TGClient


async def async_test_api_config_load():
    c = TGClient()
    assert c


def test_api_config_load():
    aio.run(async_test_api_config_load())
