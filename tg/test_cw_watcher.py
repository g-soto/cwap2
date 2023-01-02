from collections import namedtuple

import pytest

from .cw_watcher import CWWatcher

weather = ("🌙", "☀️", "☀️")
MockMessage = namedtuple("MockMessage", ("raw_text",))


@pytest.fixture
def message():
    return MockMessage(
        raw_text="In Chat Wars world now\n"
        f"{weather[0]}Evening\n"
        "18:41\n"
        "13 Winni 1074\n"
        "\n"
        "Weather forecast\n"
        f"{weather[1]}→{weather[2]}\n"
        "*Data provided by CWNN"
    )


def dummy_inform_event(*_):
    pass


def test_weather_regexp(message):
    cww = CWWatcher(dummy_inform_event)
    assert cww.is_new_weather_message(message)
    assert cww.last_weather == weather
