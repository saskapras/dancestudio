# === Stage 19: Скользящее среднее ===
# Project: DanceStudio
"""Moving-average module for DanceStudio.

Provides helpers to compute a rolling average over a numeric series
associated with a dance group. Pure standard-library implementation.
"""

from collections import deque


class MovingAverage:
    """Compute a sliding average over a sequence of numbers."""

    def __init__(self, window):
        if window <= 0:
            raise ValueError("window must be a positive integer")
        self.window = window
        self._buffer = deque(maxlen=window)

    def update(self, value):
        """Feed a new data point and return the current average."""
        self._buffer.append(value)
        return self.average()

    def average(self):
        """Return the mean of the values seen so far."""
        if not self._buffer:
            return None
        return sum(self._buffer) / len(self._buffer)

    def as_list(self):
        """Return the list of every average produced so far."""
        return [self.average() for _ in self._buffer]


def rolling_average(values, window):
    """Convenience helper: rolling mean of *values* with *window* size."""
    if window <= 0:
        raise ValueError("window must be a positive integer")
    if len(values) < window:
        raise ValueError("not enough values for the requested window")
    result = []
    for total, count in _accumulate(values, window):
        result.append(total / count)
    return result


def _accumulate(values, window):
    """Yield running sums with their valid window sizes."""
    current = 0.0
    count = 0
    for value in values:
        current += value
        count += 1
        if count < window:
            continue
        yield current, window


def group_statistics(group, metric_fn, window):
    """Rolling average of a numeric *metric_fn(group)* over time.

    *metric_fn* must accept a group and return a number. Each call
    advances the series with the group's current metric.
    """
    average = MovingAverage(window)
    series = []
    while True:
        value = metric_fn(group)
        if value is None:
            break
        series.append(average.update(value))
    return series
