#!/usr/bin/env python3

#ENPM661 Spring 2022
#Section 0101
#Jerry Pittman, Jr. UID: 117707120
#jpittma1@umd.edu
#Project #1
#solve 8-piece puzzle (3x3 grid) using Breadth First Search

import numpy as np
import copy
import timeit

#State of the Node_i represented in 3x3 matrix
#Ex: [123;456;780]
Node_State_i=[]     #The state of node i  is represented by a 3 by 3 matrix
Node_Index_i=[]         #index of node_i
Parent_Node_Index_i=[]  #index of parent_node_i
Node_Index_i.append(1)
Parent_Node_Index_i.append(0)

queue=[]                      #nodes still to be explored
Visited_Nodes=[]            #nodes that have been visited already   
x_prime=[]                  #new nodes discovered after moving blank tile
new_node=[]                 #after shifting node for saving into x_prime
BackTrackedPath=[]           #to save backtracked path

# Initial_State=[]
#------Initial State Test Cases---
#5:52PM Announcment
# Initial_State= [1,3,5,2,6,7,8,4,0]
# Initial_State= [1,2,3,4,8,6,7,5,0]

#6:32PM Announcement
# Initial_State=[1,4,7,5,0,8,2,3,6]
# Initial_State= [4,7,0,1,2,8,3,5,6]
#-----Initial State Test Cases--------

# Goal_State=[1,2,3,4,5,6,7,8,0]  #5:52PM announcement
Goal_State =[1,4,7,2,5,8,3,6,0]   #6:32PM announcement

#Breadth First Search based on possible Moves of Blank Tile
def BFSsearch(CurrentNode):
    # tmp=CurrentNode.copy()
    tmp=copy.deepcopy(CurrentNode)
    move=tmp.index(0)
    
    if(move == 0): #(0,0)
        down_node = ActionMoveDown(tmp)
        right_node = ActionMoveRight(tmp)
        new_node.append(down_node)
        new_node.append(right_node)
        return new_node
    if(move == 1):
        right_node = ActionMoveRight(tmp)
        left_node = ActionMoveLeft(tmp)
        down_node = ActionMoveDown(tmp)
        new_node.append(right_node)
        new_node.append(left_node)
        new_node.append(down_node)
        return new_node
    if(move == 2):
        down_node = ActionMoveDown(tmp)
        left_node = ActionMoveLeft(tmp)
        new_node.append(down_node)
        new_node.append(left_node)
        return new_node
    if(move == 3):
        right_node = ActionMoveRight(tmp)
        up_node = ActionMoveUp(tmp)
        down_node = ActionMoveDown(tmp)
        new_node.append(right_node)
        new_node.append(up_node)
        new_node.append(down_node)
        return new_node
    if(move == 4): #(1,1)
        right_node = ActionMoveRight(tmp)
        up_node = ActionMoveUp(tmp)
        down_node = ActionMoveDown(tmp)
        left_node = ActionMoveLeft(tmp)
        new_node.append(right_node)
        new_node.append(up_node)
        new_node.append(down_node)
        new_node.append(left_node)
        return new_node
    if(move == 5): #(1,2)
        left_node = ActionMoveLeft(tmp)
        up_node = ActionMoveUp(tmp)
        down_node = ActionMoveDown(tmp)
        new_node.append(left_node)
        new_node.append(up_node)
        new_node.append(down_node)
        return new_node
    if(move == 6):
        right_node = ActionMoveRight(tmp)
        up_node = ActionMoveUp(tmp)
        new_node.append(right_node)
        new_node.append(up_node)
        return new_node
    if(move == 7):
        right_node = ActionMoveRight(tmp)
        up_node = ActionMoveUp(tmp)
        left_node = ActionMoveLeft(tmp)
        new_node.append(right_node)
        new_node.append(up_node)
        new_node.append(left_node)
        return new_node
    if(move == 8): #(2,2)
        left_node = ActionMoveLeft(tmp)
        up_node = ActionMoveUp(tmp)
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
# ---so will go from position 3 (0,1) to 6 which is cell (1,2)
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
    
    temp_path = []
    temp_path.append(end)
    
    # pathTaken[j][0] is child Node
    # pathTaken[j][1] is parent Node
    
    c=2 #Next Node Index is 2
    for i in range(len(pathTaken)):
        Node_Index_i.append(c)      #increment child index
        
        for j in range(len(pathTaken)):

            #compare last node of temp_path to child of pathway
            if temp_path[i] == pathTaken[j][0]: #path vs child
                temp_path.append(pathTaken[j][1]) #add parent to path

                previousParent=Parent_Node_Index_i[-1] #last parent node index value
                # print("Previous parent ", previousParent)

                if pathTaken[j][1]!=pathTaken[j-1][1]:  #increment parent index if new parent
                    Parent_Node_Index_i.append(previousParent+1)
                else:
                    Parent_Node_Index_i.append(previousParent)
                # print("temp_path[i] is ", temp_path[i])
                break
            
        if temp_path[i]==start: #determine if parent is start
            break
        c+=1
    
    # print("pre-reversed_path is ", temp_path)
    # print("Parent index is ", Parent_Node_Index_i)
    # print("Node index is ", Node_Index_i)
    
    path=[]
    #reverse path so goes start to goal
    for i in reversed(temp_path):
        path.append(i)
    
    # print("reversed path is ", path)
    # print("length of path is ", len(path))
    
    return path
    
def GetInitialState():
    print("Enter values for Row 1, separated by spaces: ")
    row1=[int(x) for x in input().split()]
    print("Enter values for Row 2, separated by spaces: ")
    row2=[int(x) for x in input().split()]
    print("Enter values for Row 3, separated by spaces: ")
    row3=[int(x) for x in input().split()]
    total = row1 + row2 + row3
    return total

def makeFiles(visited, last, path, p_index, n_index):
    #Visited=Visited_Nodes, last=results
    # path=pathway, p_index=Parent_Node_Index_i, n_index=Node_Index_i
    
    #"nodePath.txt" for storing path
    f = open("NodePath.txt",'w')
    
    #convert list to String
    f.writelines("%s\n" % str(move) for move in path)
    
    f.close()
    
    #NodesInfo.txt" for storing parents and children
    f2=open('NodesInfo.txt','w')
    f2.write("Node_index\tParent_Node_index\n")
    
    for row in range(len(path)):
        f2.write(str(n_index[row]))
        f2.write("\t\t\t")
        f2.write(str(p_index[row]))
        f2.write("\n")
    f2.close()
    
    #Nodes.txt" for storing all explored states/nodes
    f3=open('Nodes.txt','w')
    
    for visit in range(len(visited)):
        f3.write(str(visited[visit]))
        f3.write("\n")
    f3.close()

#--User input for initial State---
Initial_State = GetInitialState()

print("Initial State is ", Initial_State)
queue.append(Initial_State) #start by exploring initial_state
# print("queue is ", queue)

start = timeit.default_timer()

#iteratively BFS search all tiles/nodes while queue is not empty
while (queue):
    Node_State_i=queue.pop(0) #FIFO

    # print("Queue start is ", Node_State_i)
    # print("Goal state is ", Goal_State)
    
    if np.array_equal(Node_State_i, Goal_State):
        print("Goal Reached!!")
        results=Node_State_i
        break #end while loop

    # Finds Blank tile location then perform BFS based on 
    #     possible moves in that location location
    x_prime=BFSsearch(Node_State_i)
    # print("BFS Search found ", len(x_prime), "nodes to test")
    # print("x_prime is ", x_prime)
    
    #Save Parent and Child Nodes
    for node in x_prime:
        tmp=[]
        # print("node", node)
        # print("x+prime[node]", x_prime[node])
        tmp.append(node)            #child
        tmp.append(Node_State_i)     #parent
        BackTrackedPath.append(tmp)
        # print("backTrackedPath", BackTrackedPath)
    
    #verify if new nodes discovered have been explored
    for branch in x_prime:
        # print("Branch is ", branch)
        # print("Visited_Nodes are ", Visited_Nodes)
        # print(branch not in Visited_Nodes)
        if branch not in Visited_Nodes:
            Visited_Nodes.append(branch)
            queue.append(branch)
            # print("Branch is ", branch)

    print("Visited nodes is ", len(Visited_Nodes), "long, and queue is ", len(queue))

    x_prime.clear()
    
print("BFS search Complete...Generating Path...")
stop = timeit.default_timer()
print("That search took ", stop-start, " seconds")

# print("length of pathBackwards", len(BackTrackedPath))
pathway=generate_path(Initial_State, results, BackTrackedPath)
print("Pathway is ", pathway)

print("Making .txt files..")
makeFiles(Visited_Nodes, results, pathway, Parent_Node_Index_i, Node_Index_i)
print("Program complete.")