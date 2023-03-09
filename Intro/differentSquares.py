def solution(m):
    output=set()
    for i in range(len(m)-1):
        for j in range(len(m[0])-1):
            element=tuple([m[i][j],m[i][j+1],m[i+1][j],m[i+1][j+1]])
            output.add(element)
    return len(output)
