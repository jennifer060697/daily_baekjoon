# https://www.acmicpc.net/problem/10989
# 23.06.02

import sys

def solution(input) : 
    N = int(input().strip())
    count = [0]*10001
    for _ in range(N) :
        count[int(input().strip())] += 1
    for i in range(len(count)) :
        for _ in range(count[i]) :
            sys.stdout.write(str(i)+'\n')

input = sys.stdin.readline
solution(input)