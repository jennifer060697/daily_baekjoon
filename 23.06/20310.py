# https://www.acmicpc.net/problem/20310
# 23.06.13

import sys
def solution(input) :
    line = input().strip()
    cnt1 = 0
    cnt0 = 0
    for i in line :
        if i == '1' :
            cnt1+=1
        else :
            cnt0+=1
    del1 = cnt1//2
    del0 = cnt0//2

    del1_line = ''
    for i in line :
        if i == '1' and del1 > 0 :
            del1-=1
            continue
        del1_line += i

    del0_line = ''
    for i in del1_line[::-1] :
        if i == '0' and del0 > 0 :
            del0-=1
            continue
        del0_line = i+del0_line
    print(del0_line)

input = sys.stdin.readline
solution(input)
