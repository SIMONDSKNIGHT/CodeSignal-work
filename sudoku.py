def solution(grid):
    for i in range(9):
        if len(set(grid[i]))!=9:
            return False
    for i in range(9):
        if len(set([x[i] for x in grid]))!=9:
            return False
    test=[]
    for i in range(1,9,3):
        for j in range(1,9,3):
            test.append([i,j])
    print(test)
    grids=[]
    for i in range(len(test)):
        for j in[-1,0,1]:
            for k in [-1,0,1]:


                grids.append(grid[test[i][0]+j][test[i][1]+k])
        if len(set(grids))!=9:
            return False
        grids=[]
    return True
                

