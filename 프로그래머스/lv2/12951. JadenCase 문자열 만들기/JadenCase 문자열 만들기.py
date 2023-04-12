def solution(s):
    # s     = list(s.split(" "))
    # new_s = [i.capitalize() for i in s]
    # return ' '.join(new_s)
    return ' '.join([str.capitalize() for str in s.split(" ")])