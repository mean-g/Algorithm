# def solution(k, score):
#     answer = []
#     honor  = []
    
#     for i in range(len(score)):
#         if len(honor) < k:
#             honor.append(score[i])
#             answer.append(min(honor))
#         elif score[i] > min(honor):
#             honor.append(score[i])
#             honor.remove(min(honor))
#             answer.append(min(honor))
#         else:
#             answer.append(min(honor))
            
#     return answer

def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer