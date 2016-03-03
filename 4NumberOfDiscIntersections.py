import bisect

def solution(A):
    count = 0
    a1 = [0]*len(A)
    a2 = [0]*len(A)
    for i, v in enumerate(A):
        a1[i] = i + v
        a2[i] = i - v
    a1.sort()
    a2.sort()
    for i, v in enumerate(a1):
        x = bisect.bisect_right(a2,v)
        count+=x
    #print(count)
    count -= (len(A)*(len(A)+1))/2
    if count > 10000000:
        return -1
    else:
        return count