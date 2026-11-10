print('Hello World!')

import time
from datetime import datetime, time as dtime
from zoneinfo import ZoneInfo

tz = ZoneInfo('America/Los_Angeles')
on_at = dtime(11, 30)
off_at = dtime(23, 00)
poll_rate = 1

def should_be_on(now: datetime) -> bool:
    t = now.time()
    if on_at <= off_at:
        return on_at <= t < off_at

    # this one accounts for windows of time crossing midnight
    return t >= on_at or t < off_at

def set_light(on: bool) -> None:
    # TODO: implement code to interact with the light
    print('Light On' if on else 'Light Off')

def main():
    last = None
    while True:
        try:
            current_state = should_be_on(datetime.now(tz))
            if current_state != last:
                set_light(current_state)
                last = current_state
            else:
                print('Light Steady')
        # should prevent program closing after an error
        except Exception:
            last = None
        time.sleep(poll_rate)

if __name__ == "__main__":
    main()