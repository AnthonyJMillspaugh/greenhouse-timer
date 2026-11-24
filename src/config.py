from zoneinfo import ZoneInfo
from datetime import time as dtime
from dataclasses import dataclass

# TODO: make these variables that can be changed

@dataclass
class TimerConfig:
    tz: ZoneInfo
    poll_rate: float
    start: dtime = dtime(6,00)
    end: dtime = dtime(18,00)