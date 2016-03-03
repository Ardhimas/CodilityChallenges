# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    if X > len(A):
        return -1
    exist = [0]*X
    counter = 0
    for i,v in enumerate(A):
        if(exist[v-1]==0):
            counter+=1
            exist[v-1]=1;
        if counter == X:
            return i
    return -1