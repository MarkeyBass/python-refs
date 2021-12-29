

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __repr__(self):
        return "Time(hours={}, minutes={}, seconds={})".format(
            self.hours, self.minutes, self.seconds
        )

    def __str__(self):
        return "{:02}:{:02}:{:02}".format(
            self.hours, self.minutes, self.seconds
        )

    # __cmp__ old comparison, doesn't exist in py 3

    def __eq__(self, other):
        if isinstance(other, Time):
            return (
                self.hours == other.hours
                and self.minutes == other.minutes
                and self.seconds == other.seconds
            )

        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Time):
            if self.hours > other.hours:
                return False
            elif self.hours < other.hours:
                return True
            elif self.minutes > other.minutes:
                return False
            elif self.minutes < other.minutes:
                return True
            else:
                return self.seconds < other.seconds
        else:
            return NotImplemented

    def __le__(self, other):
        return self < other or self == other

