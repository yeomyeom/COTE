input = '25 5'
n, k = map(int, input.split())

answer = 0

while 1==1:
    if n%k == 0:
        n = n / k
        answer += 1
    else:
        n = n - 1
        answer += 1
    if n == 1:
        break

#print(answer)

# 빠르게 푸는 방법
n, k = map(int, input.split())
result = 0
while True:
    #(N==K로 나누어떨어지는 수)가 될때까지 1씩 빼기
    target = (n//k) * k
    result += (n-target)
    n=target
    #N이 K보다 작을 때(더이상 나눌수 없을때) 반복문 탈출
    if n<k:
        break
    result += 1
    n //= k # 사실 몫이 몇번 나누었는지 나눈 횟수를 의미한다

result += (n-1) # 1을 만드는 건데 -1 안하면 0 만든 횟수가 나온다
print(result)
    