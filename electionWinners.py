def solution(votes, k):
    votes=sorted(votes)
    candidates=0
    
    max=votes[-1]
    if votes[-2]!=max and k==0:
        return 1
    for i in range(len(votes)-1,-1,-1) : 
        if votes[i]+k>max:
            candidates+=1
        else:
            break
    return candidates
