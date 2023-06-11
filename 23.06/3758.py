# https://www.acmicpc.net/problem/3758
# 23.06.12

import sys
def solution(input) :
    T = int(input().strip())
    
    def test(n,k,t,m) :
        log = []
        for _ in range(m) :
            log.append(list(map(int,input().split())))
        score_dict = {t:{'score_by_quiz':{0:0}, 'last_sub':0, 'sub_cnt':0}}
        for time,(i,j,s) in enumerate(log) : #제출순서,팀id,문제번호,점수
            if i in score_dict :
                score_dict[i]['last_sub'] = time
                score_dict[i]['sub_cnt'] += 1
                if j in score_dict[i]['score_by_quiz'] :
                    score_dict[i]['score_by_quiz'][j] = max(s,score_dict[i]['score_by_quiz'][j])
                else :
                    score_dict[i]['score_by_quiz'][j] = s
            else :
                score_dict[i] = {'score_by_quiz':{j:s}, 'last_sub':time, 'sub_cnt':1}
        
        # f_score,sub_cnt,last_sub,team
        for team in score_dict :
            fs = 0
            for s in score_dict[team]['score_by_quiz'].values() :
                fs+=s
            score_dict[team]['f_score'] = fs
        
        fsd = sorted(score_dict, key = lambda x : (score_dict[x]['f_score']*-1,score_dict[x]['sub_cnt'],score_dict[x]['last_sub']))

        for ans, i in enumerate(fsd) :
            if i == t :
                print(ans+1)
                return

    for _ in range(T) :
        n,k,t,m = list(map(int,input().split())) # 팀개수, 문제개수, 팀id, 엔트리수
        test(n,k,t,m)

input = sys.stdin.readline
solution(input)
