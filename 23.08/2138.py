'''
Title   : 전구와 스위치
Link    : https://www.acmicpc.net/problem/2138
Level   : G5
Problem : n번 스위치를 누르면 n-1,n,n+1 전구의 상태가 변화한다. 1번과 마지막 스위치는 2개의 스위치 상태를 변화시킨다.
          현재 전구 상태와 목적 상태가 주어질때 목적 상태가 되기 위해서 스위치를 눌러야하는 최소 횟수를 구한다.
Type    : 그리디
DATE    : 23.08.13
'''

import sys
from copy import deepcopy


def solution(input) :
    N = int(input().rstrip())
    S = input().rstrip()
    T = input().rstrip()
    
    is_same = [S[i] == T[i] for i in range(N)] # 매번 비교하지말고 모두 비교해서 배열 하나를 만들기
    
    def check(same, c) :
        count = c
        for i in range(1,N) :
            if same[i-1] : # 이전 전구가 일치하면 스킵
                continue
            else : # 이전 전구가 다르면 스위칭
                same[i] = not same[i]
                try : same[i+1] = not same[i+1]
                except : pass
                count += 1

        return count if same[-1] else -1
    
    # 1번 스위치를 누르지 않은 경우
    count = check(deepcopy(is_same), 0)

    if count != -1 : # 여기서 해답이 나왔으면 출력하고 끝내기
        print(count)
        return
        
    # 위에서 해답이 나오지 않으면
    # 1번 스위치를 누른 경우
    same = deepcopy(is_same)
    same[0] = not same[0]
    same[1] = not same[1]
    count = check(same, 1)

    print(count)

input = sys.stdin.readline
solution(input)