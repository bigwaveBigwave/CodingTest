def function(v):

    x = []
    y = []
    for vv in v:
        x.append(vv[0])
        y.append(vv[1])
    ans_x = 0
    ans_y = 0

    for xx in x:
        if x.count(xx) != 2:
            ans_x = xx

    for yy in y:
        if y.count(yy) != 2:
            ans_y = yy
    answer = []
    answer.append(ans_x)
    answer.append(ans_y)

    return answer