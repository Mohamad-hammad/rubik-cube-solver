left = [['y','o','o'],
      ['o','y','o'],
      ['o','o','y'],]
right = [['r','r','b'],
      ['r','b','r'],
      ['b','r','r'],]

up=[['g','w','w'],
       ['w', 'g', 'w'],
       ['w', 'w', 'g'],]

back=[['b','b','w'],
       ['b','w','b'],
       ['w','b','b'],]

front=[['b','g','g'],
      ['g','b','g'],
      ['g','g','b'],]

down=[['y','y','r'],
      ['y','r','y'],
      ['r','y','y'],]

# left = [['o','o','o'],
#       ['o','o','o'],
#       ['o','o','o'],]
# right = [['r','r','r'],
#       ['r','r','r'],
#       ['r','r','r'],]
#
# up=[['w','w','w'],
#        ['w', 'w', 'w'],
#        ['w', 'w', 'w'],]
#
# back=[['b','b','b'],
#        ['b','b','b'],
#        ['b','b','b'],]
#
# front=[['g','g','g'],
#       ['g','g','g'],
#       ['g','g','g'],]
#
# down=[['y','y','y'],
#       ['y','y','y'],
#       ['y','y','y'],]
def frontClockwise(up,front,right,left,back):
    temp=[0,0,0]
    temp[0], temp[1], temp[2] = front[0][0], front[0][1], front[0][2]
    front[0][0], front[0][1], front[0][2] = front[2][0], front[1][0], front[0][0]
    front[1][0], front[2][0] = front[2][1], front[2][2]
    front[2][1], front[2][2] = front[1][2], temp[2]
    front[1][2], front[0][2]=temp[1], temp[0]


    temp[0],temp[1],temp[2]=up[2][0], up[2][1], up[2][2]
    up[2][0], up[2][1], up[2][2] = left[0][2], left[1][2], left[2][2]
    left[0][2], left[1][2], left[2][2] = down[0][0], down[0][1], down[0][2]
    down[0][0], down[0][1], down[0][2] = right[0][0], right[1][0], right[2][0]
    right[0][0], right[1][0], right[2][0] = temp[0], temp[1], temp[2]

def rightClockwise(up,front,right,left,back):
    temp=[0,0,0]
    temp[0], temp[1], temp[2] = right[0][0], right[0][1], right[0][2]
    right[0][0], right[0][1], right[0][2] = right[2][0], right[1][0], right[0][0]
    right[1][0], right[2][0] = right[2][1], right[2][2]
    right[2][1], right[2][2] = right[1][2], temp[2]
    right[1][2], right[0][2] = temp[1], temp[0]

    temp[0], temp[1], temp[2] = up[0][2], up[1][2], up[2][2]
    up[0][2], up[1][2], up[2][2] =  front[0][2], front[1][2], front[2][2]
    front[0][2], front[1][2], front[2][2] = down[0][2], down[1][2], down[2][2]
    down[0][2], down[1][2], down[2][2] = back[2][0], back[1][0], back[0][0]

    back[2][0], back[1][0], back[0][0] = temp[0], temp[1], temp[2]


def upClockwise(up,front,right,left,back):
    temp = [0, 0, 0]
    temp[0], temp[1], temp[2] = up[0][0], up[0][1], up[0][2]
    up[0][0], up[0][1], up[0][2] = up[2][0], up[1][0], up[0][0]
    up[1][0], up[2][0] = up[2][1], up[2][2]
    up[2][1], up[2][2] = up[1][2], temp[2]
    up[1][2], up[0][2] = temp[1], temp[0]

    temp[0], temp[1], temp[2] = left[0][0], left[0][1], left[0][2]
    left[0][0], left[0][1], left[0][2] = front[0][0], front[0][1], front[0][2]
    front[0][0], front[0][1], front[0][2] = right[0][0], right[0][1], right[0][2]
    right[0][0], right[0][1], right[0][2] = back[0][0], back[0][1], back[0][2]
    back[0][0], back[0][1], back[0][2] = temp[0], temp[1], temp[2]

def backClockwise(up,front,right,left,back):
    temp = [0, 0, 0]
    temp[0], temp[1], temp[2] = back[0][0], back[0][1], back[0][2]
    back[0][0], back[0][1], back[0][2] = back[2][0], back[1][0], back[0][0]
    back[1][0], back[2][0] = back[2][1], back[2][2]
    back[2][1], back[2][2] = back[1][2], temp[2]
    back[1][2], back[0][2] = temp[1], temp[0]

    temp[0], temp[1], temp[2] = up[0][0], up[0][1], up[0][2]
    up[0][0], up[0][1], up[0][2] = right[0][2], right[1][2], right[2][2]
    right[0][2], right[1][2], right[2][2] = down[2][2], down[2][1], down[2][0]
    down[2][2], down[2][1], down[2][0] = left[2][0], left[1][0], left[0][0]
    left[2][0], left[1][0], left[0][0] = temp[0], temp[1], temp[2]

def leftClockwise(up,front,right,left,back):
    temp = [0, 0, 0]
    temp[0], temp[1], temp[2] = left[0][0], left[0][1], left[0][2]
    left[0][0], left[0][1], left[0][2] = left[2][0], left[1][0], left[0][0]
    left[1][0], left[2][0] = left[2][1], left[2][2]
    left[2][1], left[2][2] = left[1][2], temp[2]
    left[1][2], left[0][2] = temp[1], temp[0]

    temp[0], temp[1], temp[2] = up[0][0], up[1][0], up[2][0]
    up[0][0], up[1][0], up[2][0] = back[2][2], back[1][2], back[0][2]
    back[2][2], back[1][2], back[0][2] = down[0][0], down[1][0], down[2][0]
    down[0][0], down[1][0], down[2][0] = front[0][0], front[1][0], front[2][0]
    front[0][0], front[1][0], front[2][0] = temp[0], temp[1], temp[2]

def downClockwise(up,front,right,left,back):
    temp = [0, 0, 0]
    temp[0], temp[1], temp[2] = down[0][0], down[0][1], down[0][2]
    down[0][0], down[0][1], down[0][2] = down[2][0], down[1][0], down[0][0]
    down[1][0], down[2][0] = down[2][1], down[2][2]
    down[2][1], down[2][2] = down[1][2], temp[2]
    down[1][2], down[0][2] = temp[1], temp[0]

    temp[0], temp[1], temp[2] = back[2][0], back[2][1], back[2][2]
    back[2][0], back[2][1], back[2][2] = right[2][0], right[2][1], right[2][2]
    right[2][0], right[2][1], right[2][2] = front[2][0], front[2][1], front[2][2]
    front[2][0], front[2][1], front[2][2] = left[2][0], left[2][1], left[2][2]
    left[2][0], left[2][1], left[2][2] = temp[0], temp[1], temp[2]
def printCube(up,front,right,left,back):
    for i in range(0,3):
        print("          "+up[i][0]+" "+up[i][1]+" "+up[i][2]+" ")
    print("          " + "_" + "_" +"_" + "_"+ "_" +"_")
    for i in range(0, 3):
        print(left[i][0]+" "+left[i][1]+" "+left[i][2]+"   | "+ front[i][0]+" "+front[i][1]+" "+front[i][2]+"  | "+ right[i][0]+" "+right[i][1]+" "+right[i][2]+"  | "+
              back[i][0] + " " + back[i][1] + " " + back[i][2] + " ")
    print("          " + "_" + "_" + "_" + "_" + "_" + "_")
    for i in range(0, 3):
        print("          " + down[i][0] + " " + down[i][1] + " " + down[i][2] + " ")


#main driver code
