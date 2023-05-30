# https://www.acmicpc.net/problem/9017
# 23.05.30

def solution(input) : 
    TC = int(input().strip())
    for _ in range(TC) :
        N = int(input().strip())
        L = list(map(int,input().split()))
        teams_cnt = [0 for _ in range(201)]
        for r in L :
            teams_cnt[r]+=1
        teams_in = []
        for i in range(201) :
            if teams_cnt[i] >= 6 :
                teams_in.append(i)

        teams_score = {}
        for i in teams_in :
            teams_score[i] = []

        score = 1
        for r in L :
            if r in teams_in :
                teams_score[r].append(score)
                score+=1
        min_score = 8000
        min_score_teams = []
        for i in teams_score :
            if sum(teams_score[i][0:4]) < min_score :
                min_score_teams = [i]
                min_score = sum(teams_score[i][0:4])
            elif sum(teams_score[i][0:4]) == min_score :
                min_score_teams.append(i)
        if len(min_score_teams) == 1 :
            print(min_score_teams[0])
            continue
        min_score = 8000
        min_score_team = -1
        for i in min_score_teams :
            if teams_score[i][4] < min_score :
                min_score_team = i
                min_score = teams_score[i][4]
        print(min_score_team)
        
solution(input)