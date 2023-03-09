from collections import defaultdict
def solution(a, b, c):
    d=[a,b,c]
    dicts= defaultdict(int)
    for i in range(3):
        
        dicts[d[i]]+=1
    return min(dicts, key=dicts.get)
    
    

