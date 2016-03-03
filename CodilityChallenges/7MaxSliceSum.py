def solution(A):
    maxending = 0
    maxslice = -2147483648
    for i,v in enumerate(A,1):
        maxending = max(v,max(-2147483648,maxending+v))
        maxslice = max(maxending,maxslice)
    return maxslice