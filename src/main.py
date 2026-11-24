import logging
import time
from datetime import datetime
from scheduling import should_be_on
from hardware import set_light
from config import POLL_RATE, tz,start_time, end_time

logging.basicConfig(
    filename=r'C:/Users/tonyt/IdeaProjects/greenhouse-timer/src/timer-logs/timer.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

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