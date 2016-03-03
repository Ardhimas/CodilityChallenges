def solution(A):
    A.sort()
    for i in range (0,len(A)-2):
        if((A[i]+A[i+1])>A[i+2] and (A[i+2]+A[i+1])>A[i] and (A[i]+A[i+2])>A[i+1]):
            return 1
    return 0