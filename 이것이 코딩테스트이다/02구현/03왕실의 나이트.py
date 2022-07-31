input = 'a1'
x_pos, y_pos = input[0], input[1]
x_pos = int(ord(x_pos) - int(ord('a')) + 1)
y_pos = int(y_pos)
#print(x_pos,' ' , y_pos)
x_limit, y_limit = 8, 8

move_points = [(-1,2),(1,2),(-1,-2),(1,-2),(2,-1),(2,1),(-2,-1),(-2,1)]

answer = 0
for move_point in move_points:
    #print(move_point[0], ',', move_point[1])
    x_pos_next = x_pos + move_point[0]
    y_pos_next = y_pos + move_point[1]
    if x_pos_next >=1 and x_pos_next <=8 and y_pos_next >=1 and y_pos_next <=8:
        answer += 1

print(answer)
# 2