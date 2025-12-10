import datetime
from typing import Union

__all__ = ["utcnow", "future_time"]


def utcnow():
    """
    Returns current datetime as utc.
    """
    return datetime.datetime.now(datetime.timezone.utc)


def future_time(seconds: Union[int, float]):
    """
    Returns future time from given seconds.
    """
    return datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        seconds=seconds
    )
