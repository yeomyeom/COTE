input = '4 4'
n,m = map(int, input.split())
# 0: 육지 1: 바다

map_list = [[0]*m for _ in range(n)] # n*m 지도 만들기 
input = '1 1 0'
x, y, direct = map(int, input.split()) # x,y 좌표

# 현재 방문한 좌표는 거쳐간 곳으로 수정
answer = 1
map_list[x][y] = 1

# 왼쪽부터 가니까 서 남 동 북
x_move = [-1, 0, 1, 0]
y_move = [0, -1, 0, 1]

# 전체 맵 정보 받아오기
array = []
input = '1 1 1 1'
for i in range(n):
    array.append(list(map(int, input.split())))
input = '1 0 0 1'
for i in range(n):
    array.append(list(map(int, input.split())))
input = '1 1 0 1'
for i in range(n):
    array.append(list(map(int, input.split())))
input = '1 1 1 1'
for i in range(n):
    array.append(list(map(int, input.split())))

def turn_left(direction):
    direction -= 1
    if direction < 0:
        direction = 3
    return direction

turn_time = 0
direction = 0
while True:
    direction = turn_left(direction)
    next_x = x + map_list[direction]
    next_y = y + map_list[direction]
    if map_list[next_x][next_y] == 0 and array[next_x][next_y] == 0:
        map_list[next_x][next_y] = 1
        x = next_x
        y = next_y
        answer += 1
        turn_time = 0
    else:
        turn_time += 1

    if turn_time == 4:
        next_x = x - map_list[direction]
        next_y = y - map_list[direction]
        if array[next_x][next_y] == 0:
            x = next_x
            y = next_y
        else:
            break
        turn_time=0

print(answer)
