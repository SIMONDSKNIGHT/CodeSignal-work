def solution(v1, w1, v2, w2, maxW):
    dicts={v1:w1,v2:w2}
    if w1+w2<=maxW:
        return v1+v2
    if w1>maxW and w2>maxW:
        return 0
    return max([x for x, y in dicts.items() if y<=maxW])
             
