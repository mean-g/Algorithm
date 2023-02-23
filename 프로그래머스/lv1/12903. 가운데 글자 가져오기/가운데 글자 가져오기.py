def solution(s):
    n = len(s) // 2
    
    if len(s) % 2 == 0:
        return str(s[n-1] + s[n])
    else:
        return str(s[n])