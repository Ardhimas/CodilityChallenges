def solution(H):
    count = 0
    prevblocks = []
    minval = 1000000001
    for i,v in enumerate(H):
        if v not in prevblocks:
            count += 1
            if v < minval:
                prevblocks = [v]
                minval = v
            else:
                prevblocks.append(v)
    return count
    
def solution(H):
    count = 0
    prevblocks = []
    for i,v in enumerate(H):
        if len(prevblocks) == 0 or v > prevblocks[-1]:
            prevblocks.append(v)
            # print("appended=",v)
        elif v < prevblocks[-1]:
            while len(prevblocks) > 0 and v < prevblocks[-1]:
                count+=1
                prevblocks.pop()
                #print("lower block=",v,"len=",len(prevblocks))
                #print("count=",count)
            if len(prevblocks) == 0 or v > prevblocks[-1]:
                prevblocks.append(v)
                #print("appended",v)
    count+=len(prevblocks)
    #print("final len=",len(prevblocks))
    return count