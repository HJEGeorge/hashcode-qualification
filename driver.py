class Driver:

    def __init__(self):
        self.currentTime = 0
        self.row = 0
        self.column = 0
        self.willNextBeFree = 0

    def pick_up(self, ride):
        self.row = ride.row
        self.column = ride.column
        #willnextbefree currentTime + distance to ride