
def solution(n):
    return ( ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1) )
    #this works because the and operation of the first thing here extracts all even values and shifts them right
    #whereas the 2nd one does the same for all odd values
    #they then bitwise or them causing them to bring them together.