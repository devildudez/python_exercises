def points(games) -> int:
    x_scores=[]
    y_scores=[]
    win_x=0
    win_y=0
    for i in range(len(a)):
        s=a[i].split(":")
        x_scores.append(s[0])
        y_scores.append(s[1])
    if y_scores==3 and x_scores>y_scores:
        win_x+=1
        return win_x
    elif x_scores<y_scores:
        win_y+=1
    else:
        win_x+=1
        return win_x

a=["3:1", "2:2", "0:1"]
print(points(a))
