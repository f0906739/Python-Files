class Beaver():
    def sleep():
        pass


class Time():
    def __init__(self, days=0, hours=0, minutes=0):
        self.days = days
        self.hours = hours
        self.minutes = minutes

    def calculate_time(self):
        while self.minutes > 59:
            self.minutes -= 60
            self.hours += 1
        while self.hours > 23:
            self.hours -= 24
            self.days += 1
