
# class Node():
#     def __init__(self, parent=None, position=None, label=None):
#         self.parent = parent
#         self.position = position
#         self.label = label

#         self.g = 0
#         self.h = 0
#         self.f = 0

#     def __eq__(self, other):
#         return self.position == other.position

# def astar(list_of_point, labels, mat_adj):

#     open_list = []
#     closed_list = []
#     visited_list = []
    
#     start_node = Node(None, list_of_point[0], labels[0])
#     start_node.g = start_node.h = start_node.f = 0
    
#     end_node = Node(None, list_of_point[-1], labels[-1])
#     end_node.g = end_node.h = end_node.f = 0
    
#     open_list.append(start_node)
    
#     while len(open_list) > 0:
#         current_node = open_list[0]
#         current_index = 0
#         for index, item in enumerate(open_list):
#             if item.f < current_node.f:
#                 current_node = item
#                 current_index = index
        
#         del open_list[current_index]
#         closed_list.append(current_node)
#         visited_list.append(current_node.position)
        
#         print("cur")
#         for node in open_list:
#             print(node.label)
#         # Found the goal
#         if current_node == end_node:
#             path = []
#             current = current_node
#             while current is not None:
#                 path.append(current.label)
#                 current = current.parent
#             return path[::-1] # Return reversed path
        
#         children = []
#         neighbour_index = 0
#         print(current_index)
#         for bool in mat_adj[current_index]:
#             if bool == 1 and list_of_point[neighbour_index] not in visited_list:
#                 child_node = Node(current_node, list_of_point[neighbour_index], labels[neighbour_index])
#                 children.append(child_node)
#             neighbour_index += 1
            
#         for child in children:
            
#             for closed_child in closed_list:
#                 if child == closed_child:
#                     continue
                    
#             # Create the f, g, and h values
#             # child.g = current_node.g + haversineDistance(current_node.position, child.position)
#             # child.h = haversineDistance(end_node.position, current_node.position)
#             # child.f = child.g + child.h

#             # Child is already in the open list
#             for open_node in open_list:
#                 if child == open_node and child.g > open_node.g:
#                     continue

#             # Add the child to the open list
#             open_list.append(child)
def perms(size):
    dasar = tuple(range(1, size+1))
    length = size

    maxnumberofiter = 0
    for i in range(1,size+1):
        maxnumberofiter *= i

    arrayofnum = []
    for i in range(length):
        arrayofnum.append(i)

    perulangan = []
    for i in range(length, length-size, -1):
        perulangan.append(i)

    yield list(dasar[i] for i in arrayofnum[:size])

    count = 0
    while True or count <= maxnumberofiter:
        for i in range(size-1, -1, -1):
            perulangan[i] -= 1
            count += 1
            if perulangan[i] == 0:
                arrayofnum[i:] = arrayofnum[i+1:]+arrayofnum[i:i+1]
                perulangan[i] = length - i
            else:
                j = perulangan[i]
                swap(arrayofnum, i, -j)
                yield list(dasar[i] for i in arrayofnum[:size])
                break
        else:
            return

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return