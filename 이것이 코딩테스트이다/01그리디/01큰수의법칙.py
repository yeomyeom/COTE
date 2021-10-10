input = '5 8 3'
'리스트 컴프리헨션'
n_, m_, k_ = map(int, input.split())
input = '2 4 5 4 6'
data = list(map(int, input.split()))
'''print(n,m,k,data)'''

data.sort(reverse=True)
n=n_
m=m_
k=k_
firstBig = data[0]
seconBig = data[1]

answer = 0
# O(N) 풀이법 
while(True):
    for i in range(k):
        if m == 0:
            break
        answer += firstBig
        m -= 1
    if m == 0:
        break
    answer += seconBig
    m -= 1

print(answer)
n=n_
m=m_
k=k_
answer = 0
# 더 빠르게 푸는 방법
# 가장 큰 수가 몇번 더해지는가
count = int(m/(k+1)) * k
count += m % (k+1)

answer += count * firstBig # 큰 숫자가 더해지는 횟수
answer += (m-count) * seconBig # 두번째로 큰 숫자가 더해지는 횟수

print(answer)