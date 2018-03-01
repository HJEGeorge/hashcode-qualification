import driver
import ride
import sys
import helper

rides = []
drivers = []


def read_file(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        rows, columns, totalVehicles, totalRides, bonusPerRide, totalTime = [int(n) for n in line.split()]

        for i in range(totalVehicles):
            drivers.append(driver.Driver(i))
        for i in range(totalRides):
            line = f.readline().split()
            rides.append(ride.Ride((line[0], line[1]), (line[2], line[3]), line[4], line[5], i))

        rides.sort(key=lambda x: x.distance)
        print(rides)

        return rows, columns, totalVehicles, totalRides, bonusPerRide, totalTime


def main():
    '''
    Main function
    '''
    print(f'Running on file {sys.argv[1]}')

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <input file> <out file>")
        sys.exit()

    print('Inputting from file %s' % sys.argv[1])

    rows, columns, totalVehicles, totalRides, bonusPerRide, totalTime = read_file(sys.argv[1])

    time = 0

    for time in range(totalTime):
        print(f"Current time = {time}")
        available_drivers = list(filter(lambda x: x.isFree(time), drivers))
        available_rides = list(filter(lambda x: x.can_start(time), rides))
        for ride in available_rides:
            if len(available_drivers) > 0:
                driver = sorted(available_drivers, key=lambda x: helper.distance(x.currentLocation, ride.start))[0]
                print(f"Driver {driver.id} has picked up ride {ride.id}")
                driver.pick_up(ride)
                ride.start()



    print('Outputting to file %s' % sys.argv[2])




if __name__ == '__main__':
    main()