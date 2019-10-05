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
if __name__=='__main__':

    instances=["instance1", "instance2", "instance3", "instance4", "instance5"]

    def directions():
        instances[i].move_right()
        instances[i].move_right()
        instances[i].move_up()
        instances[i].move_right()
        instances[i].move_left()
        instances[i].move_up()
        instances[i].move_up()
        instances[i].move_down()
        instances[i].move_up()
        instances[i].move_down()
        instances[i].move_up()
    def final_x_y_coord():
        for i in range(len(instances)):
            print("\nAircraft [",i,"]")
            print("Final X-Coord:", instances[i].x)
            print("Final Y-Coord:", instances[i].y)

    for i in range(len(instances)):
        if i==0: instances[i] = Aircraft(0,0)
        if i==1: instances[i] = Aircraft(3,6)
        if i==2: instances[i] = Aircraft(6,12)
        if i==3: instances[i] = Aircraft(9,18)
        if i==4: instances[i] = Aircraft(12,24)

        print("Creating New Aircraft Object:",i)
        print("New Aircraft Object Has Just Been Initalized:",i)
        print("Initial X-Coord:",instances[i].x)
        print("Initial Y-Coord:",instances[i].y)
        directions()

    final_x_y_coord()