import random
import copy
import numpy as np
import matplotlib.pyplot as plt
'''
0 - cell is dead
1 - cell is alive
'''


def create_matrix(size):
    M = []
    for i in range(size):
        M.append([0 for e in range(size)])
    return M


def pretty_print_matrix(M):
    for row in M:
        print(row)
    print('\n')


def create_cells(M):
    for row in M:
        for ind, _ in enumerate(row):
            random_value = random.randint(1, 10)
            alive_set = {1, 2}
            if alive_set.intersection([random_value]):
                row[ind] = 1


def check_neighbours(cur_row, cur_col, M):
    neighbours_num = 0
    size = len(M)
    checking_rows = list(filter(lambda x: -1 < x < size, [cur_row - 1, cur_row, cur_row + 1]))
    checking_cols = list(filter(lambda x: -1 < x < size, [cur_col - 1, cur_col, cur_col + 1]))
    for row in checking_rows:
        for col in checking_cols:
            if row != cur_row or col != cur_col:
                neighbours_num += M[row][col]
    return neighbours_num


def cell_updated_state(is_alive, neighbours_num):
    if neighbours_num < 2 or neighbours_num > 3:
        return 0
    elif neighbours_num == 3:
        return 1
    elif neighbours_num == 2:
        if is_alive:
            return 1
        else:
            return 0


universe = np.zeros((100, 100))
create_cells(universe)
plt.ion()
while True:
    updated_universe = copy.deepcopy(universe)
    for cur_row, row in enumerate(universe):
        for cur_col, cell in enumerate(row):
            is_alive = universe[cur_row][cur_col]
            neighbours_num = check_neighbours(cur_row, cur_col, universe)
            updated_universe[cur_row][cur_col] = cell_updated_state(is_alive, neighbours_num)
    universe = updated_universe
    plt.matshow(universe, fignum=1)
    plt.draw()
    plt.pause(0.005)
    plt.clf()
