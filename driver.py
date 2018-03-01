import helper


class Driver:

    def __init__(self):
        self.currentLocation = (0, 0)
        self.willNextBeFree = 0

    def pick_up(self, time, ride):
        """increases time to show the distance travelled"""
        distance_to_ride = helper.distance(self.currentLocation, ride.start)
        self.willNextBeFree = time + distance_to_ride + ride.distance

        self.currentLocation = ride.end
