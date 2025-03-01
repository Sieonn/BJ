def soultion(v):
    x_list = [i[0] for i in v]
    y_list = [i[1] for i in v]
    x = [ i for i in x_list if x_list.count(i) == 1][0]
    y = [i for i in y_list if y_list.count(i) == 1][0]
    return [x,y]
    
print(soultion([[1,3], [3, 3], [1, 10]]))