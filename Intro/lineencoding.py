def solution(s):
    letter=''
    transient=""
    appearances=0
    for i in range(len(s)):
        if s[i]==letter:
            appearances+=1
        else:
            if appearances>1:
                transient+=str(appearances)+letter
            else:
                transient+=letter
            appearances=1
            letter=s[i]
    if appearances>1:
        transient+=str(appearances)+letter
    else:
        transient+=letter  
    return transient

        
