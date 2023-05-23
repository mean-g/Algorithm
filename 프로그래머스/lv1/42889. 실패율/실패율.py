# def solution(N, stages):
#     result      = {}
#     denominator = len(stages)
    
#     for i in range(1, N + 1):
#         if denominator != 0:
#             count     = stages.count(i)
#             result[i] = count / denominator
#             denominator -= count
#         else:
#             result[i] = 0
#     return sorted(result, key = lambda x : result[x], reverse = True)

def solution(N, stages):
    answer = []
    fail   = []
    stage   = [0] * (N + 2)
    
    for i in stages:
        stage[i] += 1
        
    for j in range(N):
        be  = sum(stage[(j + 1):])
        yet = stage[j + 1]
        if be == 0:
            fail.append((j + 1, 0))
        else:
            fail.append((j + 1, yet / be))
            
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
        
    return answer