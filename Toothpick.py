from graphics import *
class Toothpick:
    global tlength
    tlength = 63

    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __eq__(self, other):
         if other is not None:
            return self.x == other.x and self.y == other.y and self.direction == other.direction
    
    def toothpicktoAddA(self,tlist):     
        if self.direction == "horizontal":
            new_pickA = Toothpick(self.x - (tlength//2),self.y,"vertical")
        else:
            new_pickA = Toothpick(self.x, self.y- (tlength//2),"horizontal")
        
        for tpick in tlist:
            if tpick == new_pickA:
                return None
            else:
                if new_pickA.direction == "horizontal":
                    tempA = Toothpick(new_pickA.x,new_pickA.y + tlength//2,"vertical")
                    tempB = Toothpick(new_pickA.x,new_pickA.y-(tlength//2),"vertical")
                elif new_pickA.direction == "vertical":
                    tempA = Toothpick(new_pickA.x+(tlength//2),new_pickA.y,"horizontal")
                    tempB = Toothpick(new_pickA.x - (tlength//2),new_pickA.y,"horizontal")
                if tempA in tlist and tempB in tlist:
                    return None
        return new_pickA

    def toothpicktoAddB(self,tlist):
        if self.direction == "horizontal":
            new_pickB = Toothpick(self.x + (tlength//2),self.y,"vertical")
        else:
            new_pickB = Toothpick(self.x , self.y+ (tlength//2),"horizontal")
        
        for tpick in tlist:
            if tpick == new_pickB:
                return None
            else:
                if new_pickB.direction == "horizontal":
                    tempA = Toothpick(new_pickB.x,new_pickB.y + tlength//2,"vertical")
                    tempB = Toothpick(new_pickB.x,new_pickB.y-(tlength//2),"vertical")
                elif new_pickB.direction == "vertical":
                    tempA = Toothpick(new_pickB.x+(tlength//2),new_pickB.y,"horizontal")
                    tempB = Toothpick(new_pickB.x - (tlength//2),new_pickB.y,"horizontal")
                if tempA in tlist and tempB in tlist:
                    return None
        return new_pickB
    
    def show(self,win):
        if self.direction == "horizontal":
            p1 = Point(self.x - (tlength//2), self.y)
            p2 = Point(self.x + (tlength//2),self.y)
            line = Line(p1,p2)
            line.draw(win)
        else:
            p1 = Point(self.x , self.y - (tlength//2))
            p2 = Point(self.x ,self.y + (tlength//2))
            line = Line(p1,p2)
            line.draw(win)
    def __str__(self):
        return str(f"{self.x},{self.y},{self.direction}")

