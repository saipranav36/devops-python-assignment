## create an class Aircraft
class Aircraft:
    #initializing variables
    def __init__(self,x=0,y=0,ac=1):
        self.x=x
        self.y=y
        self.ac=ac
    # created methods
    def move_left(self):
        #print('moved left . . .')
        self.x = self.x - self.ac
    def move_right(self):
        #print('moved right . . .')
        self.x = self.x + self.ac
    def move_up(self):
        #print('moved up . . .')
        self.y = self.y + self.ac
    def move_down(self):
        #print('moved down . . .')
        self.y = self.y - self.ac

instances = ["instance0", "instance1", "instance2", "instance3", "instance4"]

k = len(instances)

for i in range(k):
	#instance creation
    instances[i]=Aircraft()
    print('Creating New Aircraft Object:{}'.format(i))
    print('New Aircraft Object Has Just Been Initialized:{}'.format(i))
    print('Initial X-Coord: {}'.format(instances[i].x))
    print('Initial Y-Coord: {}'.format(instances[i].y))
    
