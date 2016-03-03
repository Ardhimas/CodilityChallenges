def solution(A):
    leader = A[0]
    n = len(A)
    if n < 2:
        return 0
    size = 0
    for i,v in enumerate(A):
        if v == leader:
            size+=1
        else:
            size-=1
        if size == 0:
            leader = v
            size+=1
    leadercount = 0
    for i, v in enumerate(A):
        if v == leader:
            leadercount+=1
    
    if leadercount <= n/2:
        return 0
    
    counter = 0
    equileaders=0
    for i,v in enumerate(A):
        if v == leader:
            counter+=1
        rightsideleaders = leadercount-counter
        if counter > (i+1)/2 and rightsideleaders > (n-i-1)/2:
            equileaders+=1
    return equileaders