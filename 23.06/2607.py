# https://www.acmicpc.net/problem/2607
# 23.06.09

import sys
import copy
def solution(input) :
    def word_to_dict(word) :
        wdict = {}
        for w in word :
            if w in wdict :
                wdict[w]+=1
            else :
                wdict[w]=1
        return wdict

    def is_similer_word(main_word, word) :
        mw = copy.deepcopy(main_word)
        for w in word :
            if w in mw :
                mw[w]-=1
            else :
                mw[w]=-1
        cnts_flag = [0,0,0]
        for cnt in mw.values() :
            if cnt == 0 :
                continue
            elif (cnt == 1 or cnt == -1) and cnts_flag[cnt] == 0 :
                cnts_flag[cnt] = 1
                continue
            else :
                return 0
        return 1


    N = int(input().strip())
    words = []
    for _ in range(N) :
        words.append(input().strip())
    main_wd = word_to_dict(words[0])

    ans = 0
    for w in words[1:] :
        ans += is_similer_word(main_wd, w)
    print(ans)


input = sys.stdin.readline
solution(input)
