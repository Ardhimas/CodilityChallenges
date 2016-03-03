# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    A.sort()
    for i, v in enumerate(A):
        if(i+1 != v):
            return 0
    return 1