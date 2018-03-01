import helper


class Driver:

    def __init__(self, id):
        self.id = id
        self.currentLocation = (0, 0)
        self.willNextBeFree = 0
        self.rides = []

    def pick_up(self, time, ride):
        """increases time to show the distance travelled"""
        distance_to_ride = helper.distance(self.currentLocation, ride.start)
        self.willNextBeFree = time + distance_to_ride + ride.distance

        self.currentLocation = ride.end

        self.rides.append(ride.id)

    def is_free(self, time):
        return self.willNextBeFree <= time
