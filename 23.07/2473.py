'''
Title   : 세 용액
Link    : https://www.acmicpc.net/problem/2473
Level   : G3
Problem : 산성 용액은 1 ~ 1,000,000,000까지의 양의 정수
          알칼리성 용액은 -1 ~ -1,000,000,000까지의 음의 정수로 나타낸다.
          같은 양의 세 가지 용액을 혼합하여 특성값이 0 에 가장 가까운 용액을 만들어내는 세 용액을 찾는 프로그램을 작성한다.
Type    : 투포인터, 이분탐색
Idea    : 1. 오름차순으로 용액의 특성을 정렬한다.
          2. 맨 왼쪽 left 사용을 고정으로 하고, 나머지 용액을 투포인터를 사용하여 0과 근사하게 한다.
Date    : 23.07.20
'''

import sys


def solution1(input) :
    # 오름차순 정렬
    # 두개씩 선택
    # 뒤에꺼부터 맨 뒤까지 이진 탐색으로 0에 가까워지는걸 고르게
    # N 최악 5000
    # N*N*logN 

    def more_sim(a,b,target) :
            if abs(target-a) > abs(target-b) :
                return b
            else : return a

    def binary_find(s,target) :
        # li에서 target 값에 가까운 값 찾기
        e = len(L)-1

        
        # def recur(s,e, sim) :
        #     if s == e :
        #         if s >= len(L) :
        #             return L[-1]
        #         return more_sim(sim,L[s],target)
                
        #     mid = (e+s)//2
        #     if L[mid] == target :
        #         return target
        #     elif L[mid] < target :
        #         return recur(mid+1,e,more_sim(sim,L[mid],target))
        #     else :
        #         return recur(s,mid,more_sim(sim,L[mid],target))
            
        # return recur(s,e,L[0])

        most_sim = L[s]

        while s <= e :
            mid = (s+e) // 2
            if L[mid] == target :
                return target
            
            most_sim = more_sim(most_sim, L[mid], target)
            if L[mid] < target :
                s = mid+1
            else :
                e = mid-1
        
        return most_sim


    N = int(input().rstrip())
    L = sorted(list(map(int, input().split())))
    most_sim = L[0]+L[1]+L[2]
    most_sim_items = L[:3]

    for i in range(N-2) :
        for j in range(i+1,N-1) :
            sim = binary_find(j+1,-(L[i]+L[j]))
            
            if abs(sim + L[i] + L[j]) < abs(most_sim) :
                most_sim = abs(sim + L[i] + L[j])
                most_sim_items = [L[i], L[j], sim]

    print(' '.join([str(i) for i in most_sim_items]))


def solution2(input) :
    N = int(input().rstrip())
    L = sorted(list(map(int, input().split())))
    most_0 = abs(L[0]+L[1]+L[2])
    most_0_items = L[:3]

    for p1 in range(N-2) :
        s = p1+1
        f = N-1
        while s < f :
            newsum = L[p1]+L[s]+L[f]
            if abs(newsum) < most_0 :
                most_0 = abs(newsum)
                most_0_items = [L[p1],L[s],L[f]]
            if newsum < 0 :
                s+=1
            elif newsum > 0 :
                f-=1
            else :
                break
        if most_0 == 0 :
            break
    print(*most_0_items)

input = sys.stdin.readline
solution2(input)