def solution(n):
    val=str(n)
    maxi=0
    for i in range(len(val)):
        if int(val[:i]+val[i+1:])>maxi:
            maxi=int(val[:i]+val[i+1:])
    return maxi
        
