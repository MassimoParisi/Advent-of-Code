bingo = []
with open("input.txt") as f:
    drawn_lst = [int(x) for x in f.readline().split(',')]

    for line in f.readlines():
        if line =="\n":
            bingo.append([])
        else:
            r = [int(x) for x in line[:-1].split( )]
            bingo[-1].append(r)

num_boards = len(bingo)
winners = set()

def checkWin(board, i, j):
    flag = True
    for val in board[i]:
        if val == True:
            continue
        else:
            flag = False
    if flag:
        return True

    flag = True
    n = len(board)
    for i in range(n):
        if board[i][j] == True:
            continue
        else:
            flag = False
    return flag


def func():
    n = len(drawn_lst)

    ib, jb = len(bingo[0]), len(bingo[0][0])

    for _ in range(n):
        drawn_num = drawn_lst.pop(0)
        for idx,board in enumerate(bingo):
            if idx in winners:
                continue
            for i in range(ib):
                for j in range(jb):
                    if board[i][j] == drawn_num:
                        board[i][j] = True
                        if checkWin(board, i, j):
                            if num_boards - len(winners) == 1:        
                                unmarked = 0
                                for i2 in range(ib):
                                    for j2 in range(jb):
                                        if board[i2][j2] != True:
                                            unmarked += board[i2][j2]
                                print(f"{drawn_num=},{unmarked=}")
                                print(drawn_num*unmarked)
                                return
                            winners.add(idx)
                            print(idx)

func()

