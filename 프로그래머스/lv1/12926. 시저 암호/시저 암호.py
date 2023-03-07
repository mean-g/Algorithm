def solution(s, n):
#     lower  = "abcdefghijklmnopqrstuvwxyz"
#     upper  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     answer = ""
    
#     for i in s:
#         if i in lower:
#             j = lower.index(i) + n
#             answer += lower[j % 26]
#         elif i in upper:
#             j = upper.index(i) + n
#             answer += upper[j % 26]
#         else:
#             answer += " "
#     return answer
    answer = ''
    for i in s:
        if i >= 'A' and i <= 'Z':
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        elif i >= 'a' and i <= 'z':
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        else:
            answer += ' '
    return answer