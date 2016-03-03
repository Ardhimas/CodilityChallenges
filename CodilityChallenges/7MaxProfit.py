def solution(A):
    if len(A) < 2:
        return 0
    maxprofit = 0
    maxending = 0
    minbuy = A[0]
    maxsell = 0
    for i,v in enumerate(A,1):
        minbuy = min(minbuy,v)
        maxending = max(v-minbuy,0)
        maxprofit = max(maxprofit,maxending)
    return maxprofit