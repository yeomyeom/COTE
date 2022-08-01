input = '15 14'
n, m = map(int, input.split())
graph = []
#for idx in range(n):
#    graph.append(list(map(int, input)))
input = '00000111100000'
graph.append(list(map(int, input)))
input = '11111101111110'
graph.append(list(map(int, input)))
input = '11011101101110'
graph.append(list(map(int, input)))
input = '11011101100000'
graph.append(list(map(int, input)))
input = '11011111111111'
graph.append(list(map(int, input)))
input = '11011111111100'
graph.append(list(map(int, input)))
input = '11000000011111'
graph.append(list(map(int, input)))
input = '01111111111111'
graph.append(list(map(int, input)))
input = '00000000011111'
graph.append(list(map(int, input)))
input = '01111111111000'
graph.append(list(map(int, input)))
input = '00011111111000'
graph.append(list(map(int, input)))
input = '00000001111000'
graph.append(list(map(int, input)))
input = '11111111110011'
graph.append(list(map(int, input)))
input = '11100011111111'
graph.append(list(map(int, input)))
input = '11100011111111'
graph.append(list(map(int, input)))

print(n,',',m,',',graph)

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    else:
        if graph[x][y] == 0:
            graph[x][y] = 1 # 해당 노드 방문했다고 표시
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True
        else:
            # 벽을 만든 경우 종료
            return False

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            answer += 1

print(answer)
# 8
# DFS로 각 얼음들이 연결된 그래프라고 생각하고 풀면됨
