def solution(n):
    if n==0:
        return 10
    if n==1:
        return 1
    output=[]
    for i in range(9,1,-1):
        while n%i==0:
            n=n/i
            output.append(i)
    if n!=1:
            return -1
        
    else:
        return int("".join([str(x) for x in output[::-1]]))
