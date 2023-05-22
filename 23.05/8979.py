# https://www.acmicpc.net/problem/8979

def solution(input) : 
    N,K = list(map(int,input().split()))
    country = []
    for _ in range(N) :
        country.append(list(map(int, input().split())))
    country.sort(key=lambda x: (x[1]*-1, x[2]*-1, x[3]*-1))

    i = 0
    s = 0
    for n in range(N) :
        i+=1
        if n == 0 :
            if country[n][0] == K :
                print(i)
                return
            continue
        if country[n][1:] == country[n-1][1:] :
            i-=1
            s+=1
        elif s > 0 :
            i+=s
            s=0
        if country[n][0] == K :
            print(i)
            return

solution(input)