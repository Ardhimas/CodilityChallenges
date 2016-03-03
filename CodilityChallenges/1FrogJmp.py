def solution(X, Y, D):
    R = Y-X
    if R == 0:
        return 0
    if R%D == 0:
        return R/D
    else:
        return R/D+1