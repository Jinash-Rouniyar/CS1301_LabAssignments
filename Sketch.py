from graphics import *
from Toothpick import *
import sys

def main():
    width = height = 1000
    tlist = []
    iterations = sys.argv[1] 
    win = GraphWin("Toothpick",width,height)
    win.setBackground("white")
    t1 = Toothpick(width/2,height/2,"horizontal")
    tlist.append(t1)
    t1.show(win)
    temp_no = 1
    print("Iteration #0: Toothpicks added in this iteration: 1, Total #toothpicks: 1")
    for i in range(int(iterations)):
        temp = []
        time.sleep(0.4)
        for t1 in tlist:
            toothpickA = t1.toothpicktoAddA(tlist)
            toothpickB = t1.toothpicktoAddB(tlist)

            if toothpickA != None: 
                    toothpickA.show(win)
                    temp.append(toothpickA)

            if toothpickB != None:
                    temp.append(toothpickB)
                    toothpickB.show(win)

        tlist.extend(temp)
        print(f"Iteration #{i+1} #Toothpicks added in this iteration: {len(tlist)-temp_no}, Total #toothpicks: {len(tlist)}")
        temp_no = len(tlist)

    win.getMouse()
    win.close()
main()
