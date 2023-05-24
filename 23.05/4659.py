# https://www.acmicpc.net/problem/4659
# 23.05.24 수

def solution(input) : 
    vowels = 'aeiou'
    conson = 'bcdfghjklmnpqrstvwxyz'

    def acc_or_not(st) :
        flag1 = False
        flag = True
        for i,c in enumerate(st) :
            if c in vowels : flag1=True

            if i >= 1 :
                if st[i] == st[i-1] :
                    if c not in 'eo' :
                        flag = False
                        break 

            if i >= 2 :
                if st[i] in vowels and st[i-1] in vowels and st[i-2] in vowels :
                    flag = False
                    break
                elif st[i] in conson and st[i-1] in conson and st[i-2] in conson :
                    flag = False
                    break
        
        return flag1 and flag
    
    while True :
        st = input().strip()
        if st == 'end' : break
        sol = acc_or_not(st)
        if sol :
            print(f'<{st}> is acceptable.')
        else :
            print(f'<{st}> is not acceptable.')

solution(input)