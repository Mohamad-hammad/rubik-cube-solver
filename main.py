import copy
import collections
from collections import deque
class Game:
    Moves = ""
    Face = 0
    Back = 1
    Top = 2
    Bottom = 3
    Left = 4
    Right = 5

    Cube = 0
    def __init__(self):
        self.Cube = [[['White', 'White', 'White'], ['White', 'White', 'White'], ['White', 'White', 'White']], [['Blue', 'Blue', 'Blue'], ['Blue', 'Blue', 'Blue'], ['Blue', 'Blue', 'Blue']]]
        self.Cube.append([['Green', 'Green', 'Green'], ['Green', 'Green', 'Green'], ['Green', 'Green', 'Green']])
        self.Cube.append([['Red', 'Red', 'Red'], ['Red', 'Red', 'Red'], ['Red', 'Red', 'Red']])
        self.Cube.append([['Orange', 'Orange', 'Orange'], ['Orange', 'Orange', 'Orange'], ['Orange', 'Orange', 'Orange']])
        self.Cube.append([['Yellow', 'Yellow', 'Yellow'], ['Yellow', 'Yellow', 'Yellow'], ['Yellow', 'Yellow', 'Yellow']])
    #def __init__(self):

    def copyGame(self, instance):
        self = copy.deepcopy(instance)
        return self

    def Swap(self, a, b):
        temp = a
        temp2 = b
        return temp2, temp
#-----------------------------------Print Methods-------------------------------------
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    def PrintCube(self):
        print('\nPrinting Cube:')
        for i in range(3):
            print("\t\t\t\t\t\t"+self.Cube[self.Top][i][0] +" "+self.Cube[self.Top][i][1]+" "+self.Cube[self.Top][i][2])
        for i in range(3):
            print(self.Cube[self.Left][i][0] + " " + self.Cube[self.Left][i][1] + " " + self.Cube[self.Left][i][2]+'\t||\t'+
                  self.Cube[self.Face][i][0] + " " + self.Cube[self.Face][i][1] + " " + self.Cube[self.Face][i][2]+'\t||\t'+
                  self.Cube[self.Right][i][0] + " " + self.Cube[self.Right][i][1] + " " + self.Cube[self.Right][i][2]+'\t||\t'+
                  self.Cube[self.Back][i][0] + " " + self.Cube[self.Back][i][1] + " " + self.Cube[self.Back][i][2])
        for i in range(3):
            print("\t\t\t\t\t\t"+self.Cube[self.Bottom][i][0] +" "+self.Cube[self.Bottom][i][1]+" "+self.Cube[self.Bottom][i][2])

    def PrintCube2(self):
        print('\nPrinting Cube:')
        for i in range(3):
            print("\t\t\t"+self.Cube[self.Top][i][0][0] +" "+self.Cube[self.Top][i][1][0]+" "+self.Cube[self.Top][i][2][0])
        for i in range(3):
            print(self.Cube[self.Left][i][0][0] + " " + self.Cube[self.Left][i][1][0] + " " + self.Cube[self.Left][i][2][0]+'\t||\t'+
                  self.Cube[self.Face][i][0][0] + " " + self.Cube[self.Face][i][1][0] + " " + self.Cube[self.Face][i][2][0]+'\t||\t'+
                  self.Cube[self.Right][i][0][0] + " " + self.Cube[self.Right][i][1][0] + " " + self.Cube[self.Right][i][2][0]+'\t||\t'+
                  self.Cube[self.Back][i][0][0] + " " + self.Cube[self.Back][i][1][0] + " " + self.Cube[self.Back][i][2][0])
        for i in range(3):
            print("\t\t\t"+self.Cube[self.Bottom][i][0][0] +" "+self.Cube[self.Bottom][i][1][0]+" "+self.Cube[self.Bottom][i][2][0])

#--------------------------Move Methods-----------------------------------------------
    def MoveFace(self):
        tempArr = [0,0,0]
        for i in range(3):          #storing Right in Temp to move Top
            tempArr[i]=self.Cube[self.Right][i][0]
        for i in range(3):
            self.Cube[self.Right][i][0] = self.Cube[self.Top][2][i]
        for i in range (3):
            tempArr[i], self.Cube[self.Bottom][0][i] = self.Swap(tempArr[i], self.Cube[self.Bottom][0][i])
        for i in range (3):
            tempArr[i], self.Cube[self.Left][i][2] = self.Swap(tempArr[i], self.Cube[self.Left][i][2])
        for i in range (3):
            tempArr[i], self.Cube[self.Top][2][i] = self.Swap(tempArr[i], self.Cube[self.Top][2][i])

        # transpose of Facing side
        temp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                temp[i][j] = self.Cube[self.Face][i][j]

        self.Cube[self.Face][0][0] = temp[2][0]
        self.Cube[self.Face][0][1] = temp[1][0]
        self.Cube[self.Face][0][2] = temp[0][0]

        self.Cube[self.Face][1][2] = temp[0][1]
        self.Cube[self.Face][2][2] = temp[0][2]

        self.Cube[self.Face][2][1] = temp[1][2]
        self.Cube[self.Face][2][0] = temp[2][2]

        self.Cube[self.Face][1][0] = temp[2][1]

    def MoveTop(self):
        tempArr = [0,0,0]
        for i in range(3):
            tempArr[i]=self.Cube[self.Face][0][i]
        for i in range(3):
            self.Cube[self.Face][0][i] = self.Cube[self.Right][0][i]
        for i in range (3):
            tempArr[i], self.Cube[self.Left][0][i] = self.Swap(tempArr[i], self.Cube[self.Left][0][i])
        for i in range (3):
            tempArr[i], self.Cube[self.Back][0][i] = self.Swap(tempArr[i], self.Cube[self.Back][0][i])
        for i in range (3):
            tempArr[i], self.Cube[self.Right][0][i] = self.Swap(tempArr[i], self.Cube[self.Right][0][i])

        # transpose of Facing side
        temp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                temp[i][j] = self.Cube[self.Top][i][j]

        self.Cube[self.Top][0][0] = temp[2][0]
        self.Cube[self.Top][0][1] = temp[1][0]
        self.Cube[self.Top][0][2] = temp[0][0]

        self.Cube[self.Top][1][2] = temp[0][1]
        self.Cube[self.Top][2][2] = temp[0][2]

        self.Cube[self.Top][2][1] = temp[1][2]
        self.Cube[self.Top][2][0] = temp[2][2]

        self.Cube[self.Top][1][0] = temp[2][1]

    def MoveBack(self):
        tempArr = [0,0,0]
        for i in range(3):          #storing Right in Temp to move Top
            tempArr[i]=self.Cube[self.Right][i][2]
        for i in range(3):
            self.Cube[self.Right][i][2] = self.Cube[self.Bottom][2][i]
        for i in range (3):
            tempArr[i], self.Cube[self.Top][0][i] = self.Swap(tempArr[i], self.Cube[self.Top][0][i])
        for i in range (3):
            tempArr[i], self.Cube[self.Left][i][0] = self.Swap(tempArr[i], self.Cube[self.Left][i][0])
        for i in range (3):
            tempArr[i], self.Cube[self.Bottom][2][i] = self.Swap(tempArr[i], self.Cube[self.Bottom][2][i])

        # transpose of Facing side
        temp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
             for j in range(3):
                 temp[i][j] = self.Cube[self.Back][i][j]

        self.Cube[self.Back][0][0] = temp[2][0]
        self.Cube[self.Back][0][1] = temp[1][0]
        self.Cube[self.Back][0][2] = temp[0][0]

        self.Cube[self.Back][1][2] = temp[0][1]
        self.Cube[self.Back][2][2] = temp[0][2]

        self.Cube[self.Back][2][1] = temp[1][2]
        self.Cube[self.Back][2][0] = temp[2][2]

        self.Cube[self.Back][1][0] = temp[2][1]
    def MoveBottom(self):
        tempArr = [0,0,0]
        for i in range(3):
            tempArr[i]=self.Cube[self.Face][0][i]
        for i in range(3):
            self.Cube[self.Face][2][i] = self.Cube[self.Left][0][i]
        for i in range (3):
            tempArr[i], self.Cube[self.Right][2][i] = self.Swap(tempArr[i], self.Cube[self.Right][2][i])
        for i in range (3):
            tempArr[i], self.Cube[self.Back][2][i] = self.Swap(tempArr[i], self.Cube[self.Back][2][i])
        for i in range (3):
            tempArr[i], self.Cube[self.Left][2][i] = self.Swap(tempArr[i], self.Cube[self.Left][2][i])
        # transpose of Facing side
        temp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                temp[i][j] = self.Cube[self.Bottom][i][j]

        self.Cube[self.Bottom][0][0] = temp[2][0]
        self.Cube[self.Bottom][0][1] = temp[1][0]
        self.Cube[self.Bottom][0][2] = temp[0][0]

        self.Cube[self.Bottom][1][2] = temp[0][1]
        self.Cube[self.Bottom][2][2] = temp[0][2]

        self.Cube[self.Bottom][2][1] = temp[1][2]
        self.Cube[self.Bottom][2][0] = temp[2][2]

        self.Cube[self.Bottom][1][0] = temp[2][1]

    def MoveRight(self):
        tempArr = [0,0,0]
        for i in range(3):          #storing Right in Temp to move Top
            tempArr[i]=self.Cube[self.Back][i][0]
        for i in range(3):
            self.Cube[self.Back][i][0] = self.Cube[self.Top][i][2]
        for i in range (3):
            tempArr[i], self.Cube[self.Bottom][i][2] = self.Swap(tempArr[i], self.Cube[self.Bottom][i][2])
        for i in range (3):
            tempArr[i], self.Cube[self.Face][i][2] = self.Swap(tempArr[i], self.Cube[self.Face][i][2])
        for i in range (3):
            tempArr[i], self.Cube[self.Top][i][2] = self.Swap(tempArr[i], self.Cube[self.Top][i][2])

        # transpose of Facing side
        temp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                temp[i][j] = self.Cube[self.Right][i][j]

        self.Cube[self.Right][0][0] = temp[2][0]
        self.Cube[self.Right][0][1] = temp[1][0]
        self.Cube[self.Right][0][2] = temp[0][0]

        self.Cube[self.Right][1][2] = temp[0][1]
        self.Cube[self.Right][2][2] = temp[0][2]

        self.Cube[self.Right][2][1] = temp[1][2]
        self.Cube[self.Right][2][0] = temp[2][2]

        self.Cube[self.Right][1][0] = temp[2][1]


    def MoveLeft(self):
        tempArr = [0,0,0]
        for i in range(3):          #storing Right in Temp to move Top
            tempArr[i]=self.Cube[self.Back][i][2]
        for i in range(3):
            self.Cube[self.Back][i][2] = self.Cube[self.Bottom][i][0]
        for i in range (3):
            tempArr[i], self.Cube[self.Top][i][0] = self.Swap(tempArr[i], self.Cube[self.Top][i][0])
        for i in range (3):
            tempArr[i], self.Cube[self.Face][i][0] = self.Swap(tempArr[i], self.Cube[self.Face][i][0])
        for i in range (3):
            tempArr[i], self.Cube[self.Bottom][i][0] = self.Swap(tempArr[i], self.Cube[self.Bottom][i][0])

        # transpose of Facing side
        temp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                temp[i][j] = self.Cube[self.Left][i][j]

        self.Cube[self.Left][0][0] = temp[2][0]
        self.Cube[self.Left][0][1] = temp[1][0]
        self.Cube[self.Left][0][2] = temp[0][0]

        self.Cube[self.Left][1][2] = temp[0][1]
        self.Cube[self.Left][2][2] = temp[0][2]

        self.Cube[self.Left][2][1] = temp[1][2]
        self.Cube[self.Left][2][0] = temp[2][2]

        self.Cube[self.Left][1][0] = temp[2][1]

        #---------------------------------------Solver------------------------------

def solveCube(self, goal):
    if(self.Cube == goal.Cube):
    #if (goal.Cube[goal.Left][0][0] != 0):
        #print(goal.Cube[goal.Left][0][0])
        print("Solved")
        return goal
    queue= deque()
    queue.append(self)
    flag = True
    while (len(queue)>0)and(flag==True):
        final_node = Game()

        cur_node = queue.popleft()

        g1 = Game()

        g1 = copy.deepcopy(cur_node)

        #g1 = g1.copyGame(cur_node)
        g1.MoveLeft()
        g1.Moves+=" ->  Move Left "
        g2 = Game()

        g2 = g2.copyGame(cur_node)

        g2.MoveRight()
        g2.Moves+=" -> Move Right"
        g3 = Game()
        g3 = copy.deepcopy(cur_node)

        #g3 = g3.copyGame(cur_node)
        g3.MoveFace()
        g3.Moves+=" -> Move Face "
        g4 = Game()
        g4 = copy.deepcopy(cur_node)

        #g4 = g4.copyGame(cur_node)
        g4.MoveBottom()
        g4.Moves+=" -> Move Bottom "
        g5 = Game()
        g5 = copy.deepcopy(cur_node)

        #g5 = g5.copyGame(cur_node)
        g5.MoveTop()
        g5.Moves+=" -> Move Top "
        g6 = Game()
        g6 = copy.deepcopy(cur_node)

        #g6 = g6.copyGame(cur_node)
        g6.MoveBack()
        g6.Moves+=" -> Move Back "

        #print(type(cur_node))
        print("\nWithin Solver ")
        #cur_node.PrintCube2()

        if g1.Cube != goal.Cube:
            queue.append(g1)
        else:#else means solution found
            final_node = final_node.copyGame(g1)
            flag = False
            break
        if g2.Cube != goal.Cube:
            queue.append(g2)
        else:
            final_node = final_node.copyGame(g2)
            flag = False
            break
        if g3.Cube != goal.Cube:
            queue.append(g3)
        else:
            final_node =  final_node.copyGame(g3)
            flag = False
            break
        if g4.Cube != goal.Cube:
            queue.append(g4)
        else:
            final_node =  final_node.copyGame(g4)
            flag = False
            break
        if g5.Cube != goal.Cube:
            queue.append(g5)
        else:
            final_node = final_node.copyGame(g5)
            flag = False
            break
        if g6.Cube != goal.Cube:
            queue.append(g6)
        else:
            final_node = final_node.copyGame(g6)
            flag = False
            break

    print("\n\nSolution:")
    print(final_node.Moves)
    # for i in range(len(final_node.Moves)):
    #     print(final_node.Moves[i])
    #print(goal.Cube[goal.Left][0][0])
    print("Solved")
    return final_node
#deep copy built in function in Game class for cube
#compare built in function in Game class for cube


g1 = Game()
g1.PrintCube2()
goal = Game()

g1.MoveLeft()

g1.PrintCube2()

"""
g2 = Game()
g2 = copy.deepcopy(g1)
g2.PrintCube2()
"""

g1 = solveCube(g1,goal)
