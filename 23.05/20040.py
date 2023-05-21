from sys import stdin as s
# https://www.acmicpc.net/problem/20040
# 23.05.21

def solution(input) : 
	# 입력받기
    N, M = list(map(int, input().split())) # N : num of points, M : turns
    union_list = [i for i in range(N)]
    turns = []
    for _ in range(M) :
        turns.append(tuple(map(int, input().split())))

 	# find 구현 (점 p가 속한 그룹의 리더 찾기)
    def find(p) :
        while union_list[p] != p :
            p = union_list[p]
        return p
    # find & union : (점 p1과 p2가 속한 그룹의 리더를 찾고 리더가 서로 다르면 병합, 같으면 같다는걸 리턴)
    def union_find(p1, p2) :
        rp1 = find(p1)
        rp2 = find(p2)
        if rp1 != rp2 :
            union_list[rp2] = rp1
        else :
            return -1
            
	# 유니온 파인드 진행
    for i,(p1,p2) in enumerate(turns) :
        if union_find(p1,p2) == -1 :
            print(i+1)
            return
    print(0)
    
solution(input)