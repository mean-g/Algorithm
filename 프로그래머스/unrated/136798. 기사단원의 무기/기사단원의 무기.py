# def solution(number, limit, power):
#     answer = 0
#     divisor_knight = []

#     for k in range(1, number + 1):
#         tmp = []
#         for i in range(1,int(k**(1/2)) + 1):
#             if k % i ==0:
#                 tmp.append(i)
#                 if ( (i**2) != k) : 
#                     tmp.append(k // i)
#         divisor_knight.append(len(tmp))
    
#     for d in divisor_knight:
#         if d <= limit:
#             answer += d
#         else:
#             answer += power 

#     return answer

def cf(n):
    a = []
    
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))

def solution(number, limit, power):
    return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])