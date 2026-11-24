import pathlib
from zoneinfo import ZoneInfo
from datetime import time as dtime
from dataclasses import dataclass

# TODO: make these variables that can be changed

@dataclass
class TimerConfig:
    tz: ZoneInfo = ZoneInfo('America/Los_Angeles')
    poll_rate: int = 1
    start: dtime = dtime(6,00)
    end: dtime = dtime(18,00)

LOG_PATH = pathlib.Path(__file__).resolve().parent / 'timer-logs' / 'timer.log'