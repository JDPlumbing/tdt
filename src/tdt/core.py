# src/tdt/core.py
from datetime import datetime
from dateutil.relativedelta import relativedelta

def count_ticks(start: datetime = None, end: datetime = None, unit: str = "seconds") -> int:
    """
    Count ticks between two datetimes in the chosen unit.
    
    Args:
        start (datetime): starting time (default = Unix epoch 1970-01-01).
        end (datetime): ending time (default = now).
        unit (str): tick unit, one of:
            "years", "months", "days", "hours",
            "minutes", "seconds", "milliseconds",
            "microseconds", "nanoseconds"
    
    Returns:
        int: number of ticks between start and end.
    """
    if start is None:
        start = datetime(1970, 1, 1)
    if end is None:
        end = datetime.now()

    if unit in {"years", "months"}:
        # Use relativedelta for calendar math
        delta = relativedelta(end, start)
        if unit == "years":
            return delta.years + delta.months / 12 + delta.days / 365
        elif unit == "months":
            return delta.years * 12 + delta.months + delta.days / 30
    else:
        # Convert to timestamps for precise ticks
        delta_seconds = (end - start).total_seconds()
        if unit == "days":
            return int(delta_seconds // 86400)
        elif unit == "hours":
            return int(delta_seconds // 3600)
        elif unit == "minutes":
            return int(delta_seconds // 60)
        elif unit == "seconds":
            return int(delta_seconds)
        elif unit == "milliseconds":
            return int(delta_seconds * 1_000)
        elif unit == "microseconds":
            return int(delta_seconds * 1_000_000)
        elif unit == "nanoseconds":
            return int(delta_seconds * 1_000_000_000)
        else:
            raise ValueError(f"Unsupported unit: {unit}")

def breakdown(start: datetime, end: datetime) -> dict:
    """
    Break down elapsed time into multiple units.
    Returns dict with years, months, days, hours, minutes, seconds.
    """
    delta = relativedelta(end, start)
    return {
        "years": delta.years,
        "months": delta.months,
        "days": delta.days,
        "hours": delta.hours,
        "minutes": delta.minutes,
        "seconds": delta.seconds,
    }
