def solution(A):
    A.sort()
    negmax = A[0]*A[1]*A[-1]
    posmax = A[-1]*A[-2]*A[-3]
    if negmax>posmax:
        return negmax
    else:
        return posmax