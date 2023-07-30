'''
Title   : 빗물
Link    : https://www.acmicpc.net/problem/14719
Level   : G5
Problem : 고인 빗물의 총량을 구한다.
DATE    : 23.07.30
'''

import sys


def solution1(input) : # 위에서부터 내려오면서 해결
    H,W = map(int, input().split())
    L = list(map(int,input().split()))
    water = 0
    for h in range(H,0,-1) :
        minw, maxw = -1, -1
        for w, wh in enumerate(L) :
            if wh >= h :
                if minw == -1 : minw = w
                else : maxw = w
        if minw == -1 : continue
        elif maxw == -1 : water+=1
        else :
            water+=(maxw-minw+1)
    water-=sum(L)
    print(water)

def solution2(input) : # 왼쪽에서 오른쪽으로 가면서 해결
    H,W = map(int, input().split())
    L = list(map(int,input().split()))
    LR = list(reversed(L))
    leftmax = [0]
    rightmax = [0]
    lm = 0
    rm = 0
    for w in range(W-1) :
        lm = max(lm, L[w])
        rm = max(rm, LR[w])
        leftmax.append(lm)
        rightmax.append(rm)
    rightmax = list(reversed(rightmax))
    water=0
    for i in range(W) :
        water+=max((min(leftmax[i],rightmax[i])-L[i]),0)

    print(water)



input = sys.stdin.readline
# solution1(input)
solution2(input)