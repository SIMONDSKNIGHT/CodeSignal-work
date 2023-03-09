def solution(cell):
    cell=[ord(cell[0])-96, int(cell[1])]
    output=0
    possible=[]
    for i in [-1,1]:
        for j in [-2,2]:
            possible.append([i,j])
            possible.append([j,i])
    for i,j in possible:
        if 9>i+cell[0]>0 and 9>j+cell[1]>0:
            output+=1
    return output
        

