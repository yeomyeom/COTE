input = '5'
n = int(input)
data_ = 'R R R U D D'
data = list(map(str, data_.split()))

#print(n)
#print(data, len(data))

move_pos = ['R', 'L', 'D', 'U']
x_pos = [1, -1, 0, 0]
y_pos = [0, 0, 1, -1]
# 시작점
x, y = 1, 1

for move in data:
    for idx in range(len(move_pos)):
        if move == move_pos[idx]:
            x += x_pos[idx]
            y += y_pos[idx]
            if(x<1):
                x += 1
            elif(x>n):
                x -= 1
            if(y<1):
                y += 1
            elif(y>n):
                y -= 1
print(x,',',y)
# 3,4