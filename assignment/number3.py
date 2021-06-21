
class Lift:
    def __init__(self, maxfloor = 32, maxperson = 5):
        self.maxfloor = maxfloor
        self.maxperson = maxperson 
        self.floor = 1

    def destination(self, destinationFloor, person):
        if not self.totalPerson (person):
            return
        if (1<=destinationFloor and destinationFloor<=self.maxfloor):
            print ("going from {} to {} floor".format(self.floor, destinationFloor))
            self.floor = destinationFloor    
        else: 
            print ("Floor {} does not exist".format(destinationFloor))
    
    def totalPerson (self, person):
        if (person>self.maxperson):
            print ("Alarm on, Lift Overload")
            return False
        else: 
            print ("Door is closing")
            return True 
    
liftApartment = Lift()
destinationFloor = int(input("Input your destination Floor"))
person = int(input("Input number of person in the lift"))
liftApartment.destination(destinationFloor, person)
destinationFloor = int(input("Input your destination Floor"))
person = int(input("Input number of person in the lift"))
liftApartment.destination(destinationFloor, person)