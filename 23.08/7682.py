'''
Title   : 틱택토
Link    : https://www.acmicpc.net/problem/7682
Level   : G5
Problem : 주어진 판이 가능한 틱택토 최종 상태인지 구하기
          X가 먼저 놓는다.
Type    : 구현
DATE    : 23.08.22
'''

import sys


def solution(input) :
    # O나 X 둘중 하나만 빙고여야한다. v
    # O와 X 개수는 같거나 X가 하나 많아야한다. v
    # 빙고가 없는 경우 꽉차있어야한다. v
    # X가 빙고인 경우 X가 한개 더 많아야 한다. v
    # O가 빙고인 경우 X와 O의 개수가 같아야한다. v
    # 빙고가 2개 이상 있는 경우 모든 빙고에 겹치는 칸이 하나 있어야한다. v

    def find_bingo(board) :
        bingo_O = []
        bingo_X = []
        # 가로줄 보드 빙고 확인
        for t in range(3) :
            i = t*3
            if board[i] == board[i+1] == board[i+2] :
                if board[i] == 'O' :
                    bingo_O.append((i,i+1,i+2))
                elif board[i] == 'X' :
                    bingo_X.append((i,i+1,i+2))
        # 세로줄 보드 빙고 확인
        for t in range(3) :
            if board[t] == board[t+3] == board[t+6] :
                if board[t] == 'O' :
                    bingo_O.append((t,t+3,t+6))
                elif board[t] == 'X' :
                    bingo_X.append((t,t+3,t+6))
        # 대각선 보드 빙고 확인
        if board[0] == board[4] == board[8] :
            if board[0] == 'O' :
                bingo_O.append((0,4,8))
            elif board[0] == 'X' :
                bingo_X.append((0,4,8))
        if board[2] == board[4] == board[6] :
            if board[2] == 'O' :
                bingo_O.append((2,4,6))
            elif board[2] == 'X' :
                bingo_X.append((2,4,6))
        
        return bingo_O, bingo_X
    
    while(True) :
        board = input().rstrip()
        if board == 'end' : break
        cntO = board.count('O')
        cntX = board.count('X')
        cntdot = board.count('.')

        # O, X 개수 조건
        if not (cntO==cntX or cntO+1==cntX)  :
            print('invalid')
            continue

        bingo_O, bingo_X = find_bingo(board)

        # OX 둘다 빙고가 있는 경우
        if len(bingo_O) and len(bingo_X) :
            print('invalid')
            continue
        # OX 둘다 빙고가 없는 경우
        if not len(bingo_O) and not len(bingo_X) :
            if cntdot :
                print('invalid')
                continue
        
        if len(bingo_X) and cntX != cntO+1 :
            print('invalid')
            continue

        if len(bingo_O) and cntX != cntO :
            print('invalid')
            continue

        if len(bingo_X) >= 2 :
            for i in bingo_X[0] :
                flag = True
                for k in bingo_X[1:] :
                    if i not in k :
                        flag = False
                        break
                if flag :
                    break
                else :
                    continue
            if not flag :
                print('invalid')
                continue
        
        print('valid')

input = sys.stdin.readline
solution(input)