def solution(inputString):
    numbers=[]
    thisnumber=""
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            thisnumber+=inputString[i]
        else:
            if thisnumber!="":
                numbers.append(thisnumber)
            thisnumber=""
    if thisnumber!="":
        numbers.append(thisnumber)
    return sum([int(x) for x in numbers])

