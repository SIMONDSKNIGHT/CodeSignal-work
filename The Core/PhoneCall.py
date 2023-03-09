def solution(min1, min2_10, min11, s):
    call=0
    if s-min1<0:
        return 0
    if s>0:
        call+=1
        s-=min1
    for i in range (0,9):
        if s-min2_10<0:
            return call
        call+=1
        s-=min2_10
    while s-min11>=0:
        call+=1
        s-=min11
    return call

