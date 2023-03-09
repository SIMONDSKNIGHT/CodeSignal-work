def solution(address):
    inquotes=False
    for i in range(len(address)):
        if address[i]=='"':
            inquotes=not inquotes
        if address[i]=='@' and not inquotes:
            return address[(i+1):]
