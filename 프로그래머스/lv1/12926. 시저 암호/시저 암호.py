def solution(s, n):
    lower  = "abcdefghijklmnopqrstuvwxyz"
    upper  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ""
    
    for i in s:
        if i in lower:
            j = lower.index(i) + n
            answer += lower[j % 26]
        elif i in upper:
            j = upper.index(i) + n
            answer += upper[j % 26]
        else:
            answer += " "
    return answer