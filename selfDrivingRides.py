import driver
import ride

rides = []
drivers = []

def read_file(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        rows, columns, totalVehicles, totalRides, bonusPerRide, totalTime = [int(n) for n in line.split()]

        for i in range(totalVehicles):
            drivers.append(driver.Driver())
        for i in range(totalRides):
            


def main():
    '''
    Main function
    '''
    print(f'Running on file {sys.argv[1]}')


if __name__ == '__main__':
    main()