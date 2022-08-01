# 매번 가장 작은 숫자를 골라 맨 앞으로 보낸다는 마인드
# 선택정렬
array = [7,5,9,0,3,1,6,2,4,8]

for idx in range(len(array)):
    min_idx = idx
    for p in range(idx+1, len(array)):
        if array[min_idx] > array[p]:
            min_idx = p
        array[min_idx], array[idx] = array[idx], array[min_idx]

print(array)
# n^2