# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    if len(A) == 0:
        return 1
    A.sort()
    for i,v in enumerate(A):
        if i+1 != v:
            return i+1
    return len(A)+1