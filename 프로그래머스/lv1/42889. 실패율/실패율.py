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
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer