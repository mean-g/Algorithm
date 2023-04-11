def solution(sizes):
#     width  = []
#     length = []
    
#     for i in range(len(sizes)):
#         if sizes[i][0] < sizes[i][1]:
#             width.append(sizes[i][0])
#             length.append(sizes[i][1])
#         else:
#             width.append(sizes[i][1])
#             length.append(sizes[i][0])
#     return max(width) * max(length)
            
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)