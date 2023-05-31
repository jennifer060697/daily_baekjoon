# https://www.acmicpc.net/problem/17266
# 23.05.31

def solution(input) : 
    N = int(input().strip())
    M = int(input().strip())
    X = list(map(int,input().split()))
    min_hight = max(X[0], N-X[-1])
    for i in range(1,M) :
        mh = ((X[i] - X[i-1]) + 1) // 2 
        min_hight = max(min_hight, mh)
    print(min_hight)

solution(input)