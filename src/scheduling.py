from datetime import datetime, time as dtime

def should_be_on(now: datetime, start: dtime, end: dtime) -> bool:
    t = now.time()
    if start <= end:
        return start <= t < end

    # this one accounts for windows of time crossing midnight
    return t >= start or t < end