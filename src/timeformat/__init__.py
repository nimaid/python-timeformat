"""Provides methods to manipulate and format various time-based objects into human-readable strings."""

__version__ = "0.1.0"

from onecondition import ValidationError

from timeformat._helpers import SplitTime, split_seconds, day_of_month_suffix, day_of_month_string, timezone_name
from timeformat import dt, td
from timeformat._auto import auto
