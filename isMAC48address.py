def solution(inputString):
    pointer=0
    print(len(inputString))
    if len(inputString)!=17:
        return False
    for i in range(6):
        if valid(inputString[pointer])==False:
            return False
        pointer+=1
        if valid(inputString[pointer])==False:
            return False
        pointer+=1
        if pointer<len(inputString):
            if inputString[pointer]!="-":
                return False
        pointer+=1
    return True
        
        
def valid(chara):
    if 47<ord(chara)<58 or 64<ord(chara)<71:
        return True
    return False    
