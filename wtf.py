from random import Random
from datetime import datetime


wtf_varians = ['wtf']


def wtf_main() -> list:
    time_now = int(datetime.utcnow().timestamp())
    two_weeks = time_now + 1209600
    ban_time = Random().randint(time_now, two_weeks)
    delta = ban_time - time_now
    return [ban_time, fmt(delta)]


def fmt(t) -> str:
    days = str(int(t / 3600 / 24))
    hour = _add_lead_zero(int(t / 3600 % 24))
    mins = _add_lead_zero(int(t / 60 % 60))
    secs = _add_lead_zero(int(t / 1 % 60))
    return f"{days} days {hour}:{mins}:{secs}"


def _add_lead_zero(n) -> str:
    if n < 10:
        n = "0" + str(n)
    return n

