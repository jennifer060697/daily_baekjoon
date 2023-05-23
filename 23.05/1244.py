# https://www.acmicpc.net/problem/1244
# 23.05.23

def solution(input) : 
    N = int(input().strip())
    switch = list(map(int, input().split()))
    P = int(input().strip())
    students = []
    for _ in range(P) :
        students.append(tuple(map(int,input().split())))

    def W_switch(switch, n) :
        l = n-1
        r = n-1
        while l-1 >= 0 and r+1 < N :
            if switch[l-1] == switch[r+1] :
                l-=1
                r+=1
            else : break
        for i in range(l,r+1) :
            switch[i] = not switch[i]
    
    def M_switch(switch,n) :
        nn = n-1
        while nn < N :
            switch[nn] = not switch[nn]
            nn += n

    gender = [_, M_switch, W_switch]
    
    for g,n in students :
        gender[g](switch,n)

    sol = list(map(int,switch))
    sol_slice = [sol[i:i+20] for i in range(0,len(sol),20)]
    for s in sol_slice :
        print(' '.join(map(str,s)))

solution(input)