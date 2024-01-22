class dealership_mgmt(object):
    color = 'white'
    def __init__(self,maximum_speed,mileage):
        self.maximum_speed = maximum_speed
        self.mileage = mileage
    def seating_capacity(self,number):
        self.number = number
    def display(self):
        print('Features of vehicle:')
        print('Color of vehicle:',self.color)
        print('Maximum speed of vehicle:',self.maximum_speed)
        print('Mileage of vehicle:',self.mileage)
        print('Seating Capacity of Vehicle:',self.seating_capacity)
vehicle1 = dealership_mgmt(200,20)
vehicle1.seating_capacity(5)
vehicle1.display()
vehicle2 = dealership_mgmt(180,25)
vehicle2.seating_capacity(7)
vehicle2.display()