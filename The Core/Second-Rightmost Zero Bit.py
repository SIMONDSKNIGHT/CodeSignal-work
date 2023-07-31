def solution(n):
    return 2**([i for i, ltr in enumerate(bin(n)[:1:-1]) if ltr == '0'])[1];