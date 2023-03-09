def solution(st):
    if st == st[len(st)::-1]:
        return st
    for i in range(1,len(st)):
        print(st[len(st):i-1:-1])
        print(st[i:len(st)])
        if st[i:len(st)] == st[len(st):i-1:-1]:

            return st+st[i-1::-1]
            
