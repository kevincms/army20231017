def check_winner(board):
    # 행 확인
    for row in board:
        if board[row][0] == board[row][1] == board[row][col] and board[row][0] != ' ':
            return row[0]

    # 열 확인
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # 대각선 확인
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # 승자 없음
    return None

def block_human_win(board):
    # 행 확인
    for row in range(3):
        if board[row].count('X') == 2 and board[row].count(' ') == 1:
            return (row, board[row].index(' '))

    # 열 확인
    for col in range(3):
        column = [board[0][col], board[1][col], board[2][col]]
        if column.count('X') == 2 and column.count(' ') == 1:
            return (column.index(' '), col)

    # 대각선 확인
    diag1 = [board[0][0], board[1][1], board[2][2]]
    if diag1.count('X') == 2 and diag1.count(' ') == 1:
        return (diag1.index(' '), diag1.index(' '))
    diag2 = [board[0][2], board[1][1], board[2][0]]
    if diag2.count('X') == 2 and diag2.count(' ') == 1:
        return (diag2.index(' '), 2 - diag2.index(' '))

    # 차단 이동 없음
    return None

board = [[' ' for x in range(3)] for y in range(3)]

game_over = True
while game_over:
    for r in range(3):
        print("| " + board[r][0] + "|" + board[r][1] + " |" + board[r][2] + " |")
        if(r!=2):
            print("|--+--+--|")

    x = int(input("다음 수의 x좌표를 입력하시오(0~2): "))
    y = int(input("다음 수의 y좌표를 입력하시오(0~2): "))

    if board[x][y] != ' ':
        print("잘못된 위치입니다.")
        continue
    else:
        board[x][y] = 'X'
   
    done = False

    if block_human_win(board)!=None : board[i][j] = 'O'
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ' and not done:
                    board[i][j] = 'O'
                    done = True
                    break
    winner = check_winner(board)
    if winner!=None : game_over = False

if winner=="X" : print("ㅈ간 승")
else : print("킹갓 chargpt 승")