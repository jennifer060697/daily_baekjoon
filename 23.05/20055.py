# https://www.acmicpc.net/problem/20055
# 23.05.31

from collections import deque
def solution(input) : 
    # 입력 받기
    N,K = list(map(int, input().split()))
    S_BELT = list(map(int,input().split()))

    # deque 자료구조로 벨트 저장 (고리 구조)
    belt = deque()
    for i in S_BELT :
        belt.append([i,False])
    zeros = [0]

    def round1() :
        poped = belt.pop()
        belt.appendleft(poped)
        belt[N-1][1] = False # 내리는 위치 도달 시 내리기

    def round2() :
        for i in range(N-2,-1,-1) : # 뒤에서부터 처리
            if belt[i][1] == True and belt[i+1][1] == False and belt[i+1][0] >= 1 :
                belt[i+1][1] = True
                belt[i+1][0] -= 1
                if belt[i+1][0] == 0 :
                    zeros[0] += 1
                belt[i][1] = False
            belt[N-1][1] = False # 내리는 위치 도달 시 내리기
    
    def round3() :
        if belt[0][0] >= 1 :
            belt[0][0] -= 1
            if belt[0][0] == 0 :
                zeros[0] += 1
            belt[0][1] = True

    def round4() :
        if zeros[0] >= K :
            return True
    
    cnt = 0 # 단계
    while True :
        cnt+=1 
        round1()
        round2()
        round3()
        if round4() :
            break
    print(cnt)

solution(input)