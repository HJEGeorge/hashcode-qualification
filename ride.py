import helper


class Ride:

    def __init__(self, start, finish, earliest_start, latest_finish):
        self.start = start
        self.finish = finish
        self.earliest_pickup = earliest_start
        self.latest_pickup = latest_finish - self.distance()

    def distance(self):
        return helper.distance(self.start, self.finish)

    def can_start(self, time):
        return self.earliest_pickup <= time <= self.latest_pickup
