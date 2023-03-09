def solution(bishop, pawn):
    b=[ord(bishop[0])-96,int(bishop[1])]
    p=[ord(pawn[0])-96,int(pawn[1])]
    if abs(b[0]-p[0])==abs(b[1]-p[1]):
        return True
    return False

