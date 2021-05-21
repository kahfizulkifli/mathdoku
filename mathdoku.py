import numpy as np

def start():
    N = int(input("NxN: "))
    NCages = int(input("Number of cages: "))

    grid = []
    for i in range(N):
        nums = input().split(' ')
        nums = [int(x) for x in nums]
        grid.append(nums)

    rules = input().split(' ')
    if (len(rules) == NCages):
        rules_dict = {}
        i = 1
        for rule in rules:
            rules_dict.update({i : rule})
            i += 1

    cagePos = [[] for i in range (NCages)]
    for i in range(N):
        for j in range(N):
            index = grid[i][j]
            cagePos[index-1].append((i,j))

    board = [[0 for j in range(N)] for i in range(N)]

    return grid, rules_dict, board, cagePos, N, NCages

def checkUnique(N, board):
    for row in range(N):
        copy_row = board[row]
        row_length = len(set(copy_row)) 
        if row_length != N:
            return False

    for col in range(N):
        a = []
        for row in range(N):
            a.append(board[row][col])
        col_length = len(set(a))
        if col_length != N:
            return False

    return True

def checkCage(NCages: int, board, rules_dict: dict, cagePos):
    
        for cageNum in range(NCages):
            if (rules_dict[cageNum+1][0] == "+"):
                total = 0
                for loc in cagePos[cageNum]:
                    total += board[loc[0]][loc[1]]
                if (total != int(rules_dict[cageNum+1][1:])):
                    return False
                    break

            elif (rules_dict[cageNum+1][0]=="-"):
                loc1 = cagePos[cageNum][0]
                loc2 = cagePos[cageNum][1]
                num1 = board[loc1[0]][loc1[1]]
                num2 = board[loc2[0]][loc2[1]]
                if(abs(num1 - num2) != int(rules_dict[cageNum+1][1:])):
                    return False
                    break

            elif (rules_dict[cageNum+1][0]=="x"):
                total = 1
                for loc in cagePos[cageNum]:
                    total *= board[loc[0]][loc[1]]
                if total != int(rules_dict[cageNum+1][1:]):
                    return False
                    break
            elif (rules_dict[cageNum+1][0]=="/"):
                loc1 = cagePos[cageNum][0]
                loc2 = cagePos[cageNum][1]
                num1 = board[loc1[0]][loc1[1]]
                num2 = board[loc2[0]][loc2[1]]
                if (num1 > num2):
                    if num1/num2 != int(rules_dict[cageNum+1][1:]):
                        return False
                        break
                else:
                    if num2/num1 != int(rules_dict[cageNum+1][1:]):
                        return False   
                        break

            elif (rules_dict[cageNum+1][0]=="="):
                loc = cagePos[cageNum][0]
                if board[loc[0]][loc[1]] != int(rules_dict[cageNum+1][1:]):
                    return False
                    break
        return True