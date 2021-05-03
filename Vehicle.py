class Vehicle:
    # setters
    def __init__(self, make, model, color, fuelType, options):
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options
    
    # getters  
    def getMake(self):
        return self.make 
    def getModel(self):
        return self.model
    def getColor(self):
        return self.color
    def getFuelType(self):
        return self.fuelType
    def getOptions(self):
        return self.options
    def __str__(self):
        return f"Make:{self.make}, Model:{self.model}, Color:{self.color}, FuelType:{self.FuelType}, Options:{self.options}"

class Car(Vehicle):
   
    # setters
    def __init__(self, engineSize, numDoors):
        super().__init__(make, model, color, fuelType, options)
        self.engineSize = engineSize
        self.numDoors = numDoors
    
    # getters
    def getEngineSize(self):
        return self.engineSize
    def getNumDoors(self):
        return self.numDoors
    def __str__(self):
        return "Car: "+super(Car, self).__str__()+ ", Engine size " + str(self.enginesize) + ", NumDoors: " + str(self.numDoors)

class PickUp(Vehicle):

    # setters
    def __init__(self, cabStyle, bedLength):
        super().__init__(make, model, color, fuelType, options)
        self.cabStyle = cabStyle
        self.bedLength = bedLength

    # getters
    def getCabStyle(self):
        return self.cabStyle 
    def getBedLength(self):
        return self.bedLength
    def __str__(self):
        return "Pickup: "+super(Pickup, self).__str__() + ", Cab Style " + str(self.cabStyle) + ", Bed Length: " + str(self.bedLength)
