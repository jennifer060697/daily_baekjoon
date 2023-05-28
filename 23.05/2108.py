# https://www.acmicpc.net/problem/2108
# 23.05.28

def solution(input) : 
    # 입력받기
    N = int(input().strip())
    nlist = []
    for _ in range(N) :
        nlist.append(int(input().strip()))

    mean, median, most_custom, tigerup = 0,0,0,0 # 변수 설정
    nlist.sort()
    mean = round(sum(nlist) / N)
    median = nlist[N//2]

    # 커스텀 최빈값 구하기
    cnt = 1
    num = nlist[0]
    most = [] # nlist 배열을 (값, 횟수)] 의 배열로 표현을 치환 = most
    for i in nlist[1:] :
        if num != i :
            most.append((num,cnt))
            num = i
            cnt = 1
        else :
            cnt+=1
    most.append((num,cnt))

    most.sort(key = lambda x : (x[1]*-1,x[0])) # 횟수 기준 내림차순, 값 기준 오름차순으로 정렬

    # 최빈값이 여러개일대 두 번째로 작은 값 출력
    if len(most) > 1 and most[0][1] == most[1][1] :
        most_custom = most[1][0]
    else : most_custom = most[0][0]

    # 범위 계산
    tigerup = max(nlist) - min(nlist)

    print(mean)
    print(median)
    print(most_custom)
    print(tigerup)

solution(input)