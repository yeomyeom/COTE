# n 행 중에서 가장 작은 숫자들중 가장 큰수 

# data = list(map(int, input().split())) # 2차원 리스트 한줄씩 입력받아서 1차원 리스트로 만들기

# example1
input = '3 3'
n, m = map(int, input.split())
data = [[3,1,2],[4,1,4],[2,2,2]]
# answer = 2
# example2
#input = '2 4'
#n, m = map(int, input.split())
#data = [[7,3,1,8],[3,3,3,4]]
# answer = 3
answer = 0

for p in range(n):
    list = data[p]
    list.sort(reverse=False)
    bigNum = list[0] # 해당 행에서 가장 큰 수

    if bigNum > answer:
        answer = bigNum

print(answer)