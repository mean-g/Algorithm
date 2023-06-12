# def solution(n, m, section):
#     answer = 1
#     start  = section[0]
    
#     for i in range(1, len(section)):
#         if start + m <= section[i]:
#             answer += 1
#             start = section[i]
            
#     return answer

def solution(n, m, section):
    n = 0
    k = 0
    
    for s in section:
        if s > k:
            n += 1
            k = s+m-1
            
    return n