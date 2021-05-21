from engine import *
from mathdoku import *
from math import *
from itertools import *
import numpy as np

grid, rules_dict, board, cagePos, N, NCages = start()
brutes = list(perms(N))
order = list(permutations(range(len(brutes)), N))

solved = False

import time
start_program_time = time.time()

index = 0
while not solved and index < len(order):
    ordering = order[index]
    i = 0
    for rowindex in range(N):
        board[rowindex] = brutes[ordering[i]]
        i = i+1

    solved = checkUnique(N, board) and checkCage(NCages, board, rules_dict, cagePos)
    index += 1
    
for row in board:
    print(row)

print(str(time.time() - start_program_time)+" seconds")