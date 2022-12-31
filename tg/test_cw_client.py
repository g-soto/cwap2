from tg import TGClient
import asyncio as aio

async def async_test_api_config_load():
    c = TGClient()
    assert c

def test_api_config_load():
    aio.run(async_test_api_config_load())
