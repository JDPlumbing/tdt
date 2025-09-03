# time-delta-t

[![PyPI version](https://img.shields.io/pypi/v/time-delta-t.svg)](https://pypi.org/project/time-delta-t/)
[![Python versions](https://img.shields.io/pypi/pyversions/time-delta-t.svg)](https://pypi.org/project/time-delta-t/)
[![License](https://img.shields.io/pypi/l/time-delta-t.svg)](https://github.com/JDPlumbing/tdt/blob/main/LICENSE)

**tDt (time delta toolkit)** — a Python library for counting elapsed time in flexible, exact units.  

Think of it as a *universal stopwatch*: from milliseconds to millennia, `tDt` gives you consistent tick counts without worrying about calendars or floating-point drift.

---

## ✨ Why tDt?

Time in most software is messy:  
- Datetime APIs give you inconsistent results across months, leap years, daylight savings.  
- Floating-point math introduces rounding errors.  
- Simulations need exact, repeatable tick counts.  

`tDt` fixes this with:  

- **Deterministic results**: same input, same output — no surprises.  
- **Raw totals in all units**: years, weeks, days, seconds, down to nanoseconds.  
- **Human-readable breakdowns**: quickly see years + months + days.  
- **Simple API**: two functions cover 95% of use cases.  

---

## 🚀 Installation

```bash
pip install time-delta-t
```

---

## 🛠 Usage

### Count ticks between two dates
```python
from datetime import datetime
from tdt import count_ticks

start = datetime(2000, 1, 1)
end = datetime(2020, 1, 1)

print(count_ticks(start, end, "days"))   # → 7305
print(count_ticks(start, end, "weeks"))  # → 1043
print(count_ticks(start, end, "seconds"))# → 631152000
```

### Get a full breakdown
```python
from datetime import datetime
from tdt import breakdown_all

start = datetime(2000, 1, 1)
end = datetime(2002, 2, 15)

print(breakdown_all(start, end))
```
Output:
```python
{
  "millennia": 0,
  "centuries": 0,
  "decades": 0,
  "years": 2.12,
  "months": 25.5,
  "weeks": 111,
  "days": 780,
  "hours": 18720,
  "minutes": 1123200,
  "seconds": 67392000,
  "milliseconds": 67392000000,
  "microseconds": 67392000000000,
  "nanoseconds": 67392000000000000
}
```

### Pretty breakdown (human-friendly)
```python
from datetime import datetime
from tdt import pretty_breakdown

start = datetime(2000, 1, 1)
end = datetime(2002, 2, 15)

print(pretty_breakdown(start, end))
# → "2 years, 1 month, 14 days"
```

---

## 🔍 Use Cases

- **Simulation & modeling**  
  - Drive tick-based engines with exact elapsed cycles.  
  - e.g., count pump rotations, wire oscillations, planetary orbits.  

- **Robotics & IoT**  
  - Synchronize devices using tick counts instead of fuzzy floating time.  

- **Data processing**  
  - Express spans in whatever unit makes sense (seconds, days, months).  

- **Frontend/UI**  
  - Show users “time since install” or “lifespan remaining” in clean units.  

---

## 📖 Roadmap

- Add support for **custom tick rates** (e.g. 3600 ticks/hour = RPM).  
- Integrations with **physics/material models**.  
- Optional Rust/C++ backend for high-performance batch use.  

---

## 📝 License

Apache 2.0 © Dr. Ippy  
