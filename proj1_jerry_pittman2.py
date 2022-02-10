#ENPM661 Spring 2022
#Section 0101
#Jerry Pittman, Jr. UID: 117707120
#jpittma1@umd.edu
#Project #1
#solve 8-piece puzzle (3x3 grid)

import numpy as np


#Global variables
parent_node=[] #save previous nodes. Layer 1 is parent of layer 2.
grid_size=3 #3x3 grid_
move_status=None
moves=[]

#Enter the start and the goal positions here, in the form of a list
    #For example:
    #[[2,4,3
    #7,8,0
    #6,1,5]]
    #will be entered as : >>>> [2,4,3,7,8,0,6,1,5]
initial_state=[4,1,0,6,3,2,7,5,8]
goal_state=[1,2,3,4,5,6,7,8,0]

def moveUp(curr_node,grid_size):
    global move_status
    global moves
    node_copy = curr_node.copy()
    position = node_copy.index(0)

    num_rows = grid_size
 
    if position not in range(0, grid_size):
        #can move up
        #swap with the upper row
        tmp = curr_node[position]
        node_copy[position] = node_copy[position - num_rows]
        node_copy[position - num_rows] = tmp
        moves.append(0)
        move_status=0
        return node_copy
    else:
        return None

def moveDown(curr_node,grid_size):
    global move_status
    global moves
    node_copy = curr_node.copy()
    position = node_copy.index(0)

    num_cols = grid_size
 
    if position not in range(grid_size*(grid_size-1), grid_size*grid_size):
        #can move down
        #swap with the lower row
        tmp = curr_node[position]
        node_copy[position] = node_copy[position + num_cols]
        node_copy[position + num_cols] = tmp
        moves.append(1)
        move_status=1
        return node_copy
    else:
        return None

def moveLeft(curr_node,grid_size): 
    global move_status
    global moves
    node_copy = curr_node.copy()
    position = node_copy.index(0)
    
    #if position not in [0, 3, 6]:
    not_allowed=np.linspace(0,grid_size*(grid_size-1), grid_size, dtype=int)
    if position not in not_allowed:
        #can move left
        #swap with the left column
        tmp = curr_node[position]
        node_copy[position] = node_copy[position - 1]
        node_copy[position - 1] = tmp
        moves.append(2)
        move_status=2
        return node_copy
    else:
        return None

def moveRight(curr_node, grid_size):
    global move_status
    node_copy = curr_node.copy()
    position = node_copy.index(0)

    #if position not in [2, 5, 8]:
    not_allowed = np.linspace(grid_size-1, grid_size*grid_size - 1, grid_size, dtype = int)
    if position not in not_allowed:
        #can move right
        #swap with the right column
        tmp = curr_node[position]
        node_copy[position] = node_copy[position + 1]
        node_copy[position + 1] = tmp
        moves.append(3)
        move_status=3
        return node_copy
    else:
        return None

def getFullPath(past):
    global moves
  
    nodes = past.copy()

    moves.reverse()
    nodes.reverse()
    
    # print("moves ", moves)
    # print("nodes ", nodes)
    
    return moves, nodes

# Func to get children in all possible directions: up, down, left, right
def getBranches(node, grid_size):
    branches = []

    branches.append(moveUp(node,grid_size))
    branches.append(moveDown(node,grid_size))
    branches.append(moveLeft(node,grid_size))
    branches.append(moveRight(node,grid_size))

    #remove None nodes
    b = [branch for branch in branches if branch is not None]
    # print("b is ", b)
            
    return b

def bfsSearch(start,goal):
    grid_size=3
    global move_status
    global parent_node
    nodes_list = list() #maintain a list of all possible states till the goal is reached
    visited_nodes = list() #maintain a list of all achieved states
    
    #save initial_state node to list of all nodes (nodes_list) and visited_nodes
    nodes_list.append(start)
    
    # move priority = ["up", "down", "left", "right"]
    count=0
    
    while(nodes_list):
        current_node=nodes_list.pop()
        # print("current_node", current_node)
        visited_nodes.append(current_node)
        parent_node.append(current_node)
        # print("visted_nodes", visited_nodes)
        # print("number of visited nodes: ", len(visited_nodes))
        # print("parent nodes are ", parent_node)
        
        if np.array_equal(current_node, goal):
            print("Goal has been reached!")
            print("Total number of nodes explored:", len(visited_nodes))
            pathway, node_path = getFullPath(visited_nodes)
            # print("pathway is ", pathway)
            # print("node_path is ", node_path)
            # print("parent nodes are ", parent_node)
            return pathway, node_path

        else:
            branches = getBranches(current_node, grid_size) #get children
            

        #verify not visited already
        for branch in branches:
            if branch not in visited_nodes:
                nodes_list.insert(0,branch)
                
        count+=1

def formatAsString(state, grid_size):
    state_copy = np.array(state.copy())
    state_copy = state_copy.reshape(grid_size, grid_size)
    state_copy = state_copy.transpose()
    state_copy = state_copy.reshape(-1)
    state_copy = np.array2string(state_copy, separator=' ')
    return state_copy[1: -1]

def createPathTxtFile(pathway, nodes_list, file_names, grid_size, parent):
    path_file_name = file_names[0]
    node_file_name = file_names[1]
    parent_child_file_name = file_names[2]
    
    path_file = open(path_file_name, 'w')
    path_file.writelines("%s\n" % move for move in pathway)

    node_file = open(node_file_name, 'w')
    node_file.writelines("%s\n" % formatAsString(node, grid_size) for node in nodes_list)

    parent_child_file = open(parent_child_file_name, 'w')
    parent_child_file.writelines("NA\t")
    parent_child_file.writelines("|\t")
    parent_child_file.writelines("%s\t" % formatAsString(nodes_list[0], grid_size))
    parent_child_file.writelines("|\t")
    parent_child_file.writelines("%s\n" % formatAsString(nodes_list[1], grid_size))
    
    for i in range(1, len(nodes_list)-1):
        parent_child_file.writelines("%s\t" % formatAsString(parent[i], grid_size))
        parent_child_file.writelines("|\t")
        parent_child_file.writelines("%s\t" % formatAsString(nodes_list[i], grid_size))
        parent_child_file.writelines("|\t")
        parent_child_file.writelines("%s\n" % formatAsString(nodes_list[i+1], grid_size))

    parent_child_file.close()
    path_file.close()
    node_file.close()

#call BFS function
path, n_list = bfsSearch(initial_state, goal_state)
                
#call function to save visited notes to a file
print("storing data to .txt files ...")
save_folder_name = './Results/'
file_names = []
file_names.append(save_folder_name + "moves.txt")
file_names.append(save_folder_name + "path.txt")
file_names.append(save_folder_name + "parent_child_nodes.txt")

# print("moves are ", moves)
# U = ["up", "down", "left", "right"]
u=[]

for i in range(0,len(moves)):
    if moves[i]==0:
        u.append("up")
    elif moves[i]==1:
        u.append("down")
    elif moves[i]==2:
        u.append("left")
    elif moves[i]==3:
        u.append("right")
    
# print("u is ", u)

# print("parent nodes are ", parent_node)
createPathTxtFile(u, n_list, file_names, grid_size, parent_node)

#Print forward path in Terminal
# print("The following path was taken to go from ")
# print("Start of ", initial_state, " to ", goal_state)
# print('\nSTART ')
# print('\n')
# print(u)
# # for i in path:
# #     print(convertToMatrix(i))
# #     print('\n')
# print('GOAL')
