#!/usr/bin/env python3

#ENPM661 Spring 2022
#Section 0101
#Jerry Pittman, Jr. UID: 117707120
#jpittma1@umd.edu
#Project #1
#solve 8-piece puzzle (3x3 grid) using Breadth First Search

import numpy as np
from collections import deque
import copy

#State of the Node_i represented in 3x3 matrix
#Ex: [123;456;780]
Node_State_i=[]     #The state of node i  is represented by a 3 by 3 matrix
Node_Index_i=[]         #index of node_i
Parent_Node_Index_i=[]  #index of parent_node_i
Initial_State=[]
Goal_State=[1,2,3,4,5,6,7,8,0]

queue=deque()            #nodes still to be explored
Visited_Nodes=[]        #nodes that have been visited already   
queue_start=[]          #1st node in queue
x_prime=[]              #new nodes discovered after moving blank tile
new_node=[]             #after shifting node for saving into x_prime
BackTrackedPath=[]       #to save backtracked path

#to find location of BlankTile ("0") for moving
# def BlankTileLocation(CurrentNode):
#     #Find Blank Tile location then convert to x and y
#     tmp=CurrentNode.copy()
#     index_0=tmp.index(0)
#     # index_0=CurrentNode.index(0)
#     if (index_0 >=0 and index_0 <4):
#         x=0
#     elif (index_0>=4 and index_0 <5):
#         x=1
#     else: 
#         x=2
    
#     if (index_0==0 or index_0==3 or index_0==6):
#         y=0
#     elif (index_0==1 or index_0==4 or index_0==7):
#         y=1
#     else:
#         y=2
#     print("x is ", x, "and y is ", y)
#     return x, y
    # for x in range(len(CurrentNode)):
    #     for y in range (len(CurrentNode)):
    #         if(CurrentNode[x][y] == 0):
    #             # print ("The position of blank tile is", x , y)
    #             return [x, y]

# def DeterminePossibleMoves(blank_x,blank_y):
#     if(blank_x == 0 and blank_y == 0):
#         return 1 #can move right or down
#     elif(blank_x== 0 and blank_y == 1):
#         return 2 #can move left, right, or down
#     elif(blank_x == 0 and blank_y == 2):
#         return 3 #can move left or down
#     elif(blank_x == 1 and blank_y == 0):
#         return 4 #can move up, right, or down
#     elif(blank_x == 1 and blank_y == 1):
#         return 5 #can move up, down, left, or right
#     elif(blank_x == 1 and blank_y == 2):
#         return 6 #can move up, down, or left
#     elif(blank_x == 2 and blank_y == 0):
#         return 7 #can move up or right
#     elif(blank_x == 2 and blank_y == 1):
#         return 8 #can move left, right, or up
#     elif(blank_x == 2 and blank_y == 2):
#         return 9 #can move left or up
#     else:
#         print("Blank cannot move!!")

#Breadth First Search based on possible Moves of Blank Tile
def BFSsearch(CurrentNode):
    tmp=CurrentNode.copy()
    move=tmp.index(0)
    
    if(move == 0): #(0,0)
        down_node = ActionMoveDown(CurrentNode)
        right_node = ActionMoveRight(CurrentNode)
        new_node.append(down_node)
        new_node.append(right_node)
        return new_node
    if(move == 1):
        right_node = ActionMoveRight(CurrentNode)
        left_node = ActionMoveLeft(CurrentNode)
        down_node = ActionMoveDown(CurrentNode)
        new_node.append(right_node)
        new_node.append(left_node)
        new_node.append(down_node)
        return new_node
    if(move == 2):
        down_node = ActionMoveDown(CurrentNode)
        left_node = ActionMoveLeft(CurrentNode)
        new_node.append(down_node)
        new_node.append(left_node)
        return new_node
    if(move == 3):
        right_node = ActionMoveRight(CurrentNode)
        up_node = ActionMoveUp(CurrentNode)
        down_node = ActionMoveDown(CurrentNode)
        new_node.append(right_node)
        new_node.append(up_node)
        new_node.append(down_node)
        return new_node
    if(move == 4): #(1,1)
        right_node = ActionMoveRight(CurrentNode)
        up_node = ActionMoveUp(CurrentNode)
        down_node = ActionMoveDown(CurrentNode)
        left_node = ActionMoveLeft(CurrentNode)
        new_node.append(right_node)
        new_node.append(up_node)
        new_node.append(down_node)
        new_node.append(left_node)
        return new_node
    if(move == 5): #(1,2)
        left_node = ActionMoveLeft(CurrentNode)
        up_node = ActionMoveUp(CurrentNode)
        down_node = ActionMoveDown(CurrentNode)
        new_node.append(left_node)
        new_node.append(up_node)
        new_node.append(down_node)
        return new_node
    if(move == 6):
        right_node = ActionMoveRight(CurrentNode)
        up_node = ActionMoveUp(CurrentNode)
        new_node.append(right_node)
        new_node.append(up_node)
        return new_node
    if(move == 7):
        right_node = ActionMoveRight(CurrentNode)
        up_node = ActionMoveUp(CurrentNode)
        left_node = ActionMoveLeft(CurrentNode)
        new_node.append(right_node)
        new_node.append(up_node)
        new_node.append(left_node)
        return new_node
    if(move == 8): #(2,2)
        left_node = ActionMoveLeft(CurrentNode)
        up_node = ActionMoveUp(CurrentNode)
        new_node.append(left_node)
        new_node.append(up_node)
        return new_node
    else:
        print("Error")

def ActionMoveLeft(CurrentNode):
    # NewNode = np.copy(CurrentNode)
    NewNode = CurrentNode.copy()
    position = NewNode.index(0)
    
    tmp = NewNode[position]
    NewNode[position] = NewNode[position - 1]
    NewNode[position - 1] = tmp
    return NewNode

def ActionMoveRight(CurrentNode):
    # NewNode = np.copy(CurrentNode)
    NewNode = CurrentNode.copy()
    position = NewNode.index(0)

    tmp = NewNode[position]
    NewNode[position] = NewNode[position + 1]
    NewNode[position + 1] = tmp
    return NewNode

def ActionMoveUp(CurrentNode):
    # NewNode = np.copy(CurrentNode)
    NewNode = CurrentNode.copy()
    position = NewNode.index(0)

    tmp = NewNode[position]
    NewNode[position] = NewNode[position - 3]
    NewNode[position - 3] = tmp
    return NewNode

#To move "down", will slide the position to be 3 indexes to right
#---so will go from position 3 (0,1) to 6 which is cell (0,2)
def ActionMoveDown(CurrentNode):
    # NewNode = np.copy(CurrentNode)
    NewNode = CurrentNode.copy()
    position = NewNode.index(0)

    tmp = NewNode[position]
    NewNode[position] = NewNode[position + 3]
    NewNode[position + 3] = tmp
    return NewNode

#Convert two nodes to a string so can compare
# def compareLists(a,b):
#     A = np.copy(a)
#     B = np.copy(b)
#     X = ""
#     Y = ""
#     X = str(A[0][0])+str(A[0][1])+str(A[0][2])+str(A[1][0])+str(A[1][1])+str(A[1][2])+str(A[2][0])+str(A[2][1])+str(A[2][2])
#     Y = str(B[0][0])+str(B[0][1])+str(B[0][2])+str(B[1][0])+str(B[1][1])+str(B[1][2])+str(B[2][0])+str(B[2][1])+str(B[2][2])
#     # print("X is ", X)
#     # print("Y is ", Y)
#     if (X == Y):
#         return True
#     else:
#         return False

#backtracking to find path from initial to goal node
def generate_path(start, end, pathTaken):
    global Parent_Node_Index_i
    global Node_Index_i
    pathBackwards = []
    path=[]
    pathBackwards.append(end)
    Parent_Node_Index_i+=1
    for i in range(len(pathTaken)):
        Parent_Node_Index_i+=1
        for j in range(len(pathTaken)):
            if ((np.array_equal(pathTaken[i], pathBackwards[j][0]) )==False):
            # if isVisited(pathTaken[i],pathBackwards[j][0])==False:
                pathBackwards.append(pathTaken[j][1])
                Node_Index_i+=1
                break
            
        # Verifying if reached Initial_State yet
        if np.array_equal(start,pathTaken[j][1]):
        # if compareLists(start,pathTaken[j][1])==True:
            break
    
    #reverse path so goes start to goal
    for i in reversed(pathBackwards):
        path.append(i)

    return path

#Returns true if visited; false if not
# def isVisited(current, past):
#     beenThere = True
#     for i in range(len(current)):
#         for j in range(len(past)):
#             if(current[i][j]==past[i][j]):
#                 beenThere = True
#             else:
#                 beenThere = False
#                 break
#         if(beenThere==False):
#             break
#     # print("been there ", beenThere)
#     return beenThere
    
def GetInitialState():
    print("Enter values for Row 1, separated by spaces: ")
    row1=[int(x) for x in input().split()]
    print("Enter values for Row 2, separated by spaces: ")
    row2=[int(x) for x in input().split()]
    print("Enter values for Row 3, separated by spaces: ")
    row3=[int(x) for x in input().split()]
    total = row1 + row2 + row3
    # print("total is ", total)
    # return [row1 ,row2, row3]
    return total

def makeFiles(visited,last, path, p_index, n_index):
    #"nodePath.txt" for storing path
    f = open("Nodepath.txt",'w')
    
    #convert from column-wise matrix to list
    for i in range(len(path)):
        cell1 = path[i][0][0]
        cell2 = path[i][0][1]
        cell3 = path[i][0][2]
        cell4 = path[i][1][0]
        cell5 = path[i][1][1]
        cell6 = path[i][1][2]
        cell7 = path[i][2][0]
        cell8 = path[i][2][1]
        cell9 = path[i][2][2]
        f.write("\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n "  %(cell1,cell2,cell3,cell4,cell5,cell6,cell7,cell8,cell9))
    f.close()
    
    #NodesInfo.txt" for storing parents and children
    f2=open('NodesInfo.txt','w')
    f2.write("Node_index\tParent_Node_index")
    
    for row in range(len(path)):
        f2.write(n_index[row],"\t",p_index[row])
    f2.close()
    
    #Nodes.txt" for storing all explored states/nodes
    f3=open('Nodes.txt','w')
    
    for visit in range(len(visited)):
        f3.write(visited[visit])
    f3.close()

#User input for initial State
# Initial_State = GetInitialState()
#---For testing---
Initial_State=[1,4,7,0,2,8,3,5,6]
#---For testing---
print("Initial State is ", Initial_State)
queue.append(Initial_State) #start by exploring initial_state
# print("queue is ", queue)

count=0
#iteratively BFS search all tiles/nodes while queue is not empty
while (queue):
    queue_start=queue.popleft() #FIFO; deque is faster than pop(0)
    # queue_start=queue.pop(0) #FIFO
    # queue_start=np.copy(queue.pop(0)) #remove/get first node in queue for BFS
    print("Queue start is ", queue_start)
    # Visited_Nodes.append(queue_start)
    
    if np.array_equal(queue_start, Goal_State):
    # if (compareLists(queue_start, Goal_State)==True):
        print("Goal Reached!!")
        results=queue_start
        break #end while loop
    
    # x, y=BlankTileLocation(queue_start) #Find Location of Blank Tile ("0")
    # poss_moves=DeterminePossibleMoves(x,y)
    # print("Possible moves of blank tile is ", poss_moves)
    # print("Where 1=can move right or down, 2=can move left, right, or down, ")
    # print("3=can move left or down, 4=can move up, right, or down,")
    # print("5=can move up, down, left, or right, 6=can move up, down, or left, ")
    # print("7=can move up or right, 8=can move left, right, or up, 9=can move left or up")
    
    # position = queue_start.index(0) Find Blank Tile location
    # print("Position is ", position)
    x_prime=BFSsearch(queue_start)
    # print("BFS Search found ", len(x_prime), "nodes to test")
    
    #Save Parent and Child Nodes
    for node in range(len(x_prime)):
        tmp=[]
        tmp.append(x_prime[node]) #children
        tmp.append(queue_start) #parent\
        BackTrackedPath.append(tmp)

    
    #verify if new nodes discovered have been explored
    # previouslyVisited=False
    for branch in x_prime:
        if branch not in Visited_Nodes:
            Visited_Nodes.append(branch)
            queue.append(branch)
    
            
    print("Visited nodes is now ", len(Visited_Nodes), " long")
      
    # print("count is ", count)
    count+=1
    x_prime.clear()
    del x_prime[:] #remove all nodes from x_prime so empty for next search
    
print("while loop ended...Generating Path")
pathway=generate_path(Initial_State, results, BackTrackedPath)
print("Parent node Index is ", Parent_Node_Index_i, ", and child index is ", Node_Index_i)


makeFiles(Visited_Nodes, results, pathway)

