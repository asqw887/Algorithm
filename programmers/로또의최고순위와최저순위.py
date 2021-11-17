def rank(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    answer = []
    count = 0
    for i in lottos:
        if i in win_nums: # 안에 겹치는게 있음 
            count += 1 

    answer.append(rank(count))  # 최저순위 


    count += lottos.count(0)
    answer.insert(0,rank(count))


    return answer


    
    #다른 풀이
    '''
    def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
    
    '''