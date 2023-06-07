# https://www.acmicpc.net/problem/20529
# 23.06.07

import sys
def solution(input) :
    MBTI = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
    dist_map = [[0 for _ in range(16)] for _ in range(16)]

    def make_dist_map() :
        for i1 in range(16) :
            m1 = MBTI[i1]
            n1 = mbti_to_idx(m1)
            for i2 in range(i1,16) :
                m2 = MBTI[i2]
                n2 = mbti_to_idx(m2)
                dist = 0
                for l1,l2 in zip(m1,m2) :
                    if l1 != l2 : dist += 1
                dist_map[n1][n2] = dist
                dist_map[n2][n1] = dist


    def mbti_to_idx(mbti) :
        idx = 0
        if mbti[0] == 'I' : idx+=8
        if mbti[1] == 'N' : idx+=4
        if mbti[2] == 'T' : idx+=2
        if mbti[3] == 'P' : idx+=1
        return idx
    
    def cal_dist() :
        mbti_cnt = [0]*16
        N = int(input().strip())
        mbtis = input().split()
        for m in mbtis :
            i = mbti_to_idx(m)
            mbti_cnt[i] += 1
            if mbti_cnt[i] >= 3 :
                return 0
        idxs = []
        for i in range(16) :
            n = mbti_cnt[i]
            for _ in range(n) :
                idxs.append(i)
        dists = []
        for i in range(len(idxs)) :
            mi = idxs[i]
            for j in range(i+1,len(idxs)) :
                mj = idxs[j]
                for k in range(j+1,len(idxs)) :
                    mk = idxs[k]
                    d = 0
                    d+=dist_map[mi][mj]
                    d+=dist_map[mj][mk]
                    d+=dist_map[mk][mi]
                    dists.append(d)
        return min(dists)
        

    make_dist_map()
    
    T = int(input().strip())
    for _ in range(T) :
        print(cal_dist())

input = sys.stdin.readline
solution(input)
