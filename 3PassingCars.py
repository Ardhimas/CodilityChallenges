def solution(A):
    eastcount = 0
    passcount = 0
    for i,v in enumerate(A):
        if(v == 0):
            eastcount+=1
        if(v == 1):
            passcount+=eastcount
    if(passcount <= 1000000000):
        return passcount
    else:
        return -1