def print_brdard(brd):

    for i in range(len(brd)):
        if i%3 == 0 and i != 0:
            print('- - - - - - - - - - - - - ')

        for j in range(len(brd[0])):
            if j%3 == 0 and j != 0:
                print(' | ', end="")

            if j == 8:
                print(brd[i][j])

            else:
                print(str(brd[i][j]) + " ", end='')

def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j) #row, col

    return None

def is_valid(brd, num, pos):

    #check row
    for i in range(len((brd[0]))):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    #check 3x3 grid
    brdx_x = pos[1] // 3
    brdx_y = pos[0] // 3

    for i in range(brdx_y*3, brdx_y*3+3):
        for j in range(brdx_x*3, brdx_x*3+3):
            if brd[i][j] == num and (i,j) != pos:
                return False

    return True


def solve(brd):

    find = find_empty(brd)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if is_valid(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0


    return False

test = [
       [2, 0, 0, 0, 7, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 2, 7, 3, 4],
       [4, 6, 7, 0, 0, 8, 0, 0, 9],
       [0, 0, 0, 9, 1, 0, 0, 0, 8],
       [0, 1, 0, 0, 8, 7, 0, 0, 0],
       [0, 8, 6, 2, 5, 4, 1, 0, 7],
       [0, 0, 8, 3, 4, 0, 0, 2, 0],
       [9, 4, 0, 0, 2, 0, 8, 5, 0],
       [6, 5, 0, 0, 9, 0, 4, 0, 0]
       ]

print_brdard(test)
solve(test)
print("__________________________________")
print_brdard(test)


