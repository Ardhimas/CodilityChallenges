def solution(A, B):
    count = len(A)
    downfish = []
    for i, v in enumerate(A):
        if B[i] == 1:
            downfish.append(v)
        elif B[i] == 0:
            while(len(downfish)>0 and downfish[-1]<v):
                count-=1
                downfish.pop()
            if(len(downfish)>0 and downfish[-1]>v):
                count-=1
    return count