# Time Formatting Tools
### Provides methods to manipulate and format various time-based objects into human-readable strings in Python.
[![Python Version](https://img.shields.io/pypi/pyversions/timefmt?logo=python&logoColor=white)](https://pypi.org/project/timefmt/)
[![PyPI Version](https://img.shields.io/pypi/v/timefmt?logo=PyPI&logoColor=white)](https://pypi.org/project/timefmt/)

[![GitHub Build](https://img.shields.io/github/actions/workflow/status/nimaid/python-timeformat/master.yml?logo=GitHub)](https://github.com/nimaid/python-timeformat/actions/workflows/master.yml)
[![Coveralls Coverage](https://img.shields.io/coverallsCoverage/github/nimaid/python-timeformat?logo=coveralls)](https://coveralls.io/github/nimaid/python-timeformat)
[![Codecov Coverage](https://codecov.io/gh/nimaid/python-timeformat/graph/badge.svg?token=IG0GJD2GIO)](https://codecov.io/gh/nimaid/python-timeformat)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1315b052266245688caf4c9869bb2ad9)](https://app.codacy.com/gh/nimaid/python-timeformat/dashboard)

[![License](https://img.shields.io/pypi/l/timefmt?logo=opensourceinitiative&logoColor=white)](https://github.com/nimaid/python-timeformat/raw/main/LICENSE)
[![PyPI Downloads](https://img.shields.io/pypi/dm/timefmt.svg?label=pypi%20downloads&logo=PyPI&logoColor=white)](https://pypi.org/project/timefmt/)



## Usage

```python
import datetime
import timefmt

now = datetime.datetime.now()

print("Now (short):", timefmt.dt.short(now))
print("Now (long):", timefmt.dt.long(now))

since_epoch = datetime.timedelta(seconds=now.timestamp())

print("Time since Jan. 1st, 1970 (short):", timefmt.td.short(since_epoch))
print("Time since Jan. 1st, 1970 (long):", timefmt.td.long(since_epoch))

# You can also automatically detect which type it is, like so
import random

random_choice = random.choice([now, since_epoch])

print("Unknown time format value (short):", timefmt.auto(random_choice))
print("Unknown time format value (long):", timefmt.auto(random_choice, long=True))
```
This prints the following:
```
Now (short): 11:12:12 AM
Now (long): 11:12:12 AM US Mountain Standard Time
Time since Jan. 1st, 1970 (short): 2817W 2D 18:12:12
Time since Jan. 1st, 1970 (long): 2817 weeks, 2 days, 18 hours, 12 minutes, and 12 seconds
Unknown time format value (short): 11:12:12 AM
Unknown time format value (long): 11:12:12 AM US Mountain Standard Time
```

# Full Documentation
<p align="center"><a href="https://timefmt.readthedocs.io/en/latest/index.html"><img src="https://brand-guidelines.readthedocs.org/_images/logo-wordmark-vertical-dark.png" width="300px" alt="timefmt on Read the Docs"></a></p>
