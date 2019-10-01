## create an class Aircraft
class Aircraft:
    #initializing variables
    def __init__(self,x=0,y=0,ac=1):
        self.x=x
        self.y=y
        self.ac=ac
    # created methods
    def move_left(self):
        print('moved left . . .')
        self.x = self.x - self.ac
    def move_right(self):
        print('moved right . . .')
        self.x = self.x + self.ac
    def move_up(self):
        print('moved up . . .')
        self.y = self.y + self.ac
    def move_down(self):
        print('moved down . . .')
        self.y = self.y - self.ac
# created one obj instance
obj= Aircraft()
#printing intial values
print('Initial X-Coord: {}'.format(obj.x))
print('Initial Y-Coord: {}'.format(obj.y))

# calling functions with object
obj.move_up()
obj.move_up()
obj.move_up()
obj.move_right()
obj.move_right()
obj.move_down()
obj.move_left()

#printing final values
print('Final X-Coord: {}'.format(obj.x))
print('Final Y-Coord: {}'.format(obj.y))