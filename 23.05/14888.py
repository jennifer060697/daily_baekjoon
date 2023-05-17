# https://www.acmicpc.net/problem/14888
# 23.05.17 8:51 AM!
def solution(input) : 
    def plus(a,b) :
        return a+b
    def minus(a,b) :
        return a-b
    def multi(a,b) :
        return a*b
    def divi(a,b) :
        if a<0 :
            return -((-a)//b)
        else :
            return a//b
    oper = [plus, minus, multi, divi]
    
    N = int(input())
    num = list(map(int,input().split()))
    oper_max_cnt = list(map(int, input().split()))
    global cal_f
    cal_f = []
    def recur(i, cal, cnt) : # i : 현재 연산해야하는 인덱스 번호 (0~N-1)
        global cal_f
        if i >= N :
            cal_f.append(cal)
            return
        for o in range(4) :
            ncnt = cnt.copy()
            if ncnt[o] < oper_max_cnt[o] :
                ncnt[o]+=1
                ncal = oper[o](cal, num[i])
                recur(i+1, ncal, ncnt)
    
    recur(1,num[0],[0,0,0,0])
    print(max(cal_f))
    print(min(cal_f))

solution(input)
