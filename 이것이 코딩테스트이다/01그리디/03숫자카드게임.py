input = '3 3'
n , m = map(int, input.split())
input = '''3 1 2
4 1 4 
2 2 2 '''
# 답2

input = '2 4'
n , m = map(int, input.split())
input = '''7 3 1 8
3 3 3 4
'''
# 답3
answer = 0
dataInput = list(map(int, input.split()))
for i in range(n):
    data = dataInput[m*i:m*i+m]
    minVal = min(data)
    answer = max(minVal, answer)

print(answer)
