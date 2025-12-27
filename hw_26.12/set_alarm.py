def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    if employed == False and vacation == False:
        return False
    if employed == True and vacation == True:
        return False
    if employed == False and vacation == True:
        return False


print(set_alarm(True, True))
print(set_alarm(False, True))