def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    
    for idx, num in enumerate(eng):
        if num in s:
            s = s.replace(num, str(idx))
        answer = s
    return int(answer)