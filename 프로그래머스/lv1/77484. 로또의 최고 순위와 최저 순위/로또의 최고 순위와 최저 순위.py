# def solution(lottos, win_nums):
#     new_lottos = list(set(lottos + win_nums))
#     unknown    = lottos.count(0)
#     rank       = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}
    
#     if 0 in new_lottos:
#         new_lottos.remove(0)
        
#     return rank[12 - len(new_lottos)], rank[12 - len(new_lottos) - unknown]

def solution(lottos, win_nums):
    rank    = [6, 6, 5, 4, 3, 2, 1]
    unknown = lottos.count(0)
    result  = 0
    
    for i in win_nums:
        if i in lottos:
            result += 1
    return rank[result + unknown], rank[result]