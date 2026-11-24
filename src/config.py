from zoneinfo import ZoneInfo
from datetime import time as dtime

# TODO: make these variables that can be changed

start_time = dtime(6, 00)
end_time = dtime(18, 00)

tz = ZoneInfo('America/Los_Angeles')
POLL_RATE = 1