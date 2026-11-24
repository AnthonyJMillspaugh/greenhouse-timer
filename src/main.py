import logging
import time
from datetime import datetime
from scheduling import should_be_on
from hardware import set_light
from config import TimerConfig, LOG_PATH

LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

def main():
    last = None
    while True:
        try:
            current_state = should_be_on(datetime.now(TimerConfig.tz), TimerConfig.start, TimerConfig.end)
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
        time.sleep(TimerConfig.poll_rate)

if __name__ == "__main__":
    main()