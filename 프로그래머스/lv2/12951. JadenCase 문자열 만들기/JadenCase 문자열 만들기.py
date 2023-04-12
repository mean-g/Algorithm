def solution(s):
    s = list(s.split(" "))
    new_s = [i.capitalize() for i in s]
    return ' '.join(new_s)