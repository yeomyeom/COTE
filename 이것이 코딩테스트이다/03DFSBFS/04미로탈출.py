input = '5 6'
n, m = map(int, input.split())
graph = []
input = '101010'
graph.append(list(map(int, input)))
input = '111111'
graph.append(list(map(int, input)))
input = '000001'
graph.append(list(map(int, input)))
input = '111111'
graph.append(list(map(int, input)))
input = '111111'
graph.append(list(map(int, input)))

from collections import deque
# 상, 하, 좌, 우
x_pos = [0, 0, -1, 1]
y_pos = [1, -1, 0, 0]

# 출발점에서 가까운 노드부터 먼저 방문하니 BFS 알고리즘으로 접근
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            next_x = x + x_pos[i]
            next_y = y + y_pos[i]
            if next_x >= 0 and next_x < n and next_y >=0 and next_y < m:
                if graph[next_x][next_y] == 1:
                    graph[next_x][next_y] = graph[x][y] + 1 # 출발 노드로부터 몇 번째 노드인가
                    queue.append((next_x, next_y))
    return graph[n-1][m-1]

print(bfs(0,0))
# 10

