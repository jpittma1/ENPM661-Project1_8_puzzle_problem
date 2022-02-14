#!/usr/bin/env python3

#ENPM661 Spring 2022
#Section 0101
#Jerry Pittman, Jr. UID: 117707120
#jpittma1@umd.edu
#Project #1
#solve 8-piece puzzle (3x3 grid) using Breadth First Search

from xml.etree.ElementTree import TreeBuilder
import numpy as np
from collections import deque
import copy
import timeit

#State of the Node_i represented in 3x3 matrix
#Ex: [123;456;780]
Node_State_i=[]     #The state of node i  is represented by a 3 by 3 matrix
Node_Index_i=[]         #index of node_i
Parent_Node_Index_i=[]  #index of parent_node_i
# Initial_State=deque()
Initial_State=list()
# Goal_State=deque([1,2,3,4,5,6,7,8,0])
Goal_State=[1,2,3,4,5,6,7,8,0]

# queue=deque()            #nodes still to be explored
# Visited_Nodes=deque()        #nodes that have been visited already   
# queue_start=deque()          #1st node in queue
# x_prime=deque()              #new nodes discovered after moving blank tile
# new_node=deque()             #after shifting node for saving into x_prime
# BackTrackedPath=deque()       #to save backtracked path
queue=list()                  #nodes still to be explored
Visited_Nodes=list()            #nodes that have been visited already   
queue_start=list()              #1st node in queue
x_prime=list()                  #new nodes discovered after moving blank tile
new_node=list()               #after shifting node for saving into x_prime
BackTrackedPath=list()           #to save backtracked path

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
    NewNode = CurrentNode.copy()
    position = NewNode.index(0)
    
    tmp = NewNode[position]
    NewNode[position] = NewNode[position - 1]
    NewNode[position - 1] = tmp
    return NewNode

def ActionMoveRight(CurrentNode):
    NewNode = CurrentNode.copy()
    position = NewNode.index(0)

    tmp = NewNode[position]
    NewNode[position] = NewNode[position + 1]
    NewNode[position + 1] = tmp
    return NewNode

def ActionMoveUp(CurrentNode):
    NewNode = CurrentNode.copy()
    position = NewNode.index(0)

    tmp = NewNode[position]
    NewNode[position] = NewNode[position - 3]
    NewNode[position - 3] = tmp
    return NewNode

# To move "down", will slide the position to be 3 indexes to right
# ---so will go from position 3 (0,1) to 6 which is cell (0,2)
def ActionMoveDown(CurrentNode):
    NewNode = CurrentNode.copy()
    position = NewNode.index(0)

    tmp = NewNode[position]
    NewNode[position] = NewNode[position + 3]
    NewNode[position + 3] = tmp
    return NewNode

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
    return deque(total)

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
# Initial_State=[1,4,7,0,2,8,3,5,6]
Initial_State=[1,4,7,0,2,8,3,5,6]
#---For testing---
print("Initial State is ", Initial_State)
queue.append(Initial_State) #start by exploring initial_state
# print("queue is ", queue)

start = timeit.default_timer()


count=0
#iteratively BFS search all tiles/nodes while queue is not empty
while (queue):
# while (count<700):
    # Node_State_i=queue.copy()
    queue_start=queue.pop(0)
    # queue_start=queue.popleft() #FIFO; deque is faster than pop(0)
    # queue_start=np.copy(queue.popleft())

    # print("Queue start is ", queue_start)
    # print("Goal state is ", Goal_State)
 
    # Visited_Nodes.append(queue_start)
    
    if np.array_equal(queue_start, Goal_State):
        print("Goal Reached!!")
        results=queue_start
        break #end while loop
    
    #Secondary test to verify if goal state reached/found
    if queue_start==Goal_State: 
        print("Goal Reached!!")
        results=queue_start
        break #end while loop
    
    
    # Finds Blank tile location then perform BFS based on 
    # possible moves in that location location
    x_prime=BFSsearch(queue_start)
    # print("BFS Search found ", len(x_prime), "nodes to test")
    # print("x_prime is ", x_prime)
    
    #Save Parent and Child Nodes
    for node in range(len(x_prime)):
        tmp=list()
        # print("node", node)
        # print("x+prime[node]", x_prime[node])
        tmp.append(x_prime[node]) #children
        tmp.append(queue_start) #parent\
        BackTrackedPath.append(tmp)
        # print("backTrackedPath", BackTrackedPath)
    
    #verify if new nodes discovered have been explored
    # for branch in x_prime:
    #     # print("Branch is ", branch)
    #     # print("Visited_Nodes are ", Visited_Nodes)
    #     if branch not in Visited_Nodes:
    #         Visited_Nodes.append(branch)
    #         queue.append(branch)
            # print("Branch is ", branch)
    
    
    # for i in range(len(x_prime)):
    #     y = False
    #     # print("i is ", i)
    #     # print("visited Nodes length" ,len(Visited_Nodes))
    #     for j in range(len(Visited_Nodes)):
            # y = np.array_equal(x_prime[i], Visited_Nodes[j])       #if same, then True (have visited)
    #         # print("np array equal is ", np.array_equal(x_prime[i], Visited_Nodes[j]))
    #         # print("j is ", j)
    #         # print("y of ", i, ", ",j, " loop is ", y)
    #         # print("Branch is ", x_prime[i])
    #         # print("Visit[j] is ",Visited_Nodes[j])
            
    #         if(y == False):
    #             # print("New value of X'")
    #             break
    #     # print("Y in i loop is ", y)
    #     if(y == False):
    #         Visited_Nodes.append(x_prime[i])   # In case the new node hasn't been explored storage is Virtual_Node
    #         queue.append(x_prime[i])
    #         # print("queue is now ",queue)
    #     else:
    #         print("Finally visited Node!! @", x_prime[i])
            
    for i in range(len(x_prime)):
        y = False
        # z=False
        # print("i is ", i)
        # print("visited Nodes length" ,len(Visited_Nodes))
        for j in range(len(Visited_Nodes)):
            # z = np.array_equal(x_prime[i], Visited_Nodes[j])       #if same, then True (have visited)
            # print("np array equal is ", np.array_equal(x_prime[i], Visited_Nodes[j]))
            # print("j is ", j)
            # print("y of ", i, ", ",j, " loop is ", y)
            # print("Branch is ", x_prime[i])
            # print("Visit[j] is ",Visited_Nodes[j])
            if(x_prime[i] != Visited_Nodes[j]):
            # if(x_prime[i] != Visited_Nodes[j] or z==False):
                # print("New value of X'")
                y=False
                break
        # print("Y in i loop is ", y)
        if(y == False):
            Visited_Nodes.append(x_prime[i])   # In case the new node hasn't been explored storage is Virtual_Node
            queue.append(x_prime[i])
            # print("queue is now ",queue)
        else:
            print("Finally a visited Node!! @", x_prime[i])                
    
            
    print("Visited nodes is now ", len(Visited_Nodes), " long")
      
    # print("count is ", count)
    count+=1
    x_prime.clear()
    # del x_prime[:] #remove all nodes from x_prime so empty for next search
    
print("while loop ended...Generating Path..")
stop = timeit.default_timer()
print("That search took ", stop-start)

pathway=generate_path(Initial_State, results, BackTrackedPath)
print("Parent node Index is ", Parent_Node_Index_i, ", and child index is ", Node_Index_i)


makeFiles(Visited_Nodes, results, pathway)

