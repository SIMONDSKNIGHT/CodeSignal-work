def solution(text):
    index=0
    length=0
    max_length=0
    for i in range(len(text)):
        if text[i].isalpha():
            length+=1
            if length>max_length:
                index=i-(length-1)
                max_length=length
        else:
            length=0
    return text[index:index+max_length]

