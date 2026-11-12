print('Hello World!')

import logging
import time
from datetime import datetime, time as dtime
from zoneinfo import ZoneInfo

tz = ZoneInfo('America/Los_Angeles')
POLL_RATE = 1

logging.basicConfig(
    filename=r'C:/Users/tonyt/IdeaProjects/greenhouse-timer/src/timer-logs/timer.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

# TODO: make these variables that can be changed
class TimeMarker:
    def __init__(self, time: dtime, start: bool):
        self.time = time
        self.start = start

start_time = TimeMarker(time = dtime(6, 00), start = True)
end_time = TimeMarker(time = dtime(18, 00), start = False)
def should_be_on(now: datetime, start: TimeMarker, end: TimeMarker) -> bool:
    t = now.time()
    if start.time <= end.time:
        return start.time <= t < end.time

    # this one accounts for windows of time crossing midnight
    return t >= start.time or t < end.time

def set_light(on: bool) -> None:
    # TODO: implement code to interact with the light
    print('Light On' if on else 'Light Off')

def main():
    last = None
    while True:
        try:
            current_state = should_be_on(datetime.now(tz), start_time, end_time)
            if current_state != last:
                set_light(current_state)
                logging.info("Light -> %s", "ON" if current_state else "OFF")
                last = current_state
            else:
                print('Light Steady')
        # should prevent program closing after an error
        except Exception:
            logging.exception('Error; will retry')
            last = None
        time.sleep(POLL_RATE)

if __name__ == "__main__":
    main()