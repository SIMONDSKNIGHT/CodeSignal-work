def solution(time):
    if 0<=int(time[:2])<24 and 0<=int(time[3:])<60:
        return True
    return False

