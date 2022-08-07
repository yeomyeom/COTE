#import sys
#input = sys.stdin.readline().rstrip()
input = '4 6'
n,m = map(int, input.split())
input = '19 15 10 17'
array = list(map(int, input.split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 떡을 자른 구간이 얼마나 잘렸는지 확인
        if x > mid:
            total += x - mid
    if total >= m:
        # 정답인 경우
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
    
