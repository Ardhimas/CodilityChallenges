def solution(A):
    if(len(A) < 4):
        return 0
    A.pop()
    A.pop(0)
    # print(A)
    maxsum = A[0]
    minval = A[0]
    realmax = -10000
    for i, v in enumerate(A[1:]):
        # print(maxsum," ",v)
        if v > maxsum+v:
            minval = min(v,10000)
            maxsum = v
        else:
            minval = min(v,minval)
            maxsum+=v
        # print("maxsum=",maxsum)
        realmax = max(realmax,(maxsum-minval))
    return realmax