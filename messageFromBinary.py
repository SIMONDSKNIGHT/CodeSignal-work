def solution(code):
    output=""
    for i in range(0,len(code),8):
        output+=chr(int(code[i:i+8],base=2))
    return output
        
