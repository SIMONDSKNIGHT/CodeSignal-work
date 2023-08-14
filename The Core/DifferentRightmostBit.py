def solution(n, m):
    return 2**(len(bin(int(bin(n)[2:],2)^int(bin(m)[2:],2))) - (bin(int(bin(n)[2:],2)^int(bin(m)[2:],2)).rindex("1")+1));
