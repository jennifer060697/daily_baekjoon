'''
Title   : 탑
Link    : https://www.acmicpc.net/problem/2493
Level   : G5
Problem : 모든 탑의 꼭대기에서 왼쪽으로 신호를 보낸다. 신호를 받는 탑의 위치를 출력한다.
Type    : 스택
Idea    : 앞에서부터 검사를 진행한다. 스택에는 부딪힐 수 있는 탑들만 남긴다.
          스택의 원소가 검사할 탑보다 낮다면 pop한다.
          새 원소를 스택에 추가한다.
TC      : O(N). 약 2N이라고 생각된다.
'''

import sys


def solution(input) :
    N = int(input().rstrip())
    towers = list(map(int, input().split()))
    answer = [0]*N
    stack = [0]

    for i in range(1,N) :
        while stack and towers[stack[-1]] < towers[i] :
            del stack[-1]
        if stack : answer[i] = stack[-1]+1
        stack.append(i)
    
    #print(*answer)
    print(" ".join(map(str, answer)))

input = sys.stdin.readline
solution(input)