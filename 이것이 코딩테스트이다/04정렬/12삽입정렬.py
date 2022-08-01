# 적절한 위치가 보일때만 이동 시작
# 삽입정렬
array = [7,5,9,0,3,1,6,2,4,8]
# step1 7은 정렬됨 5가 어디갈지 생각 -> 7보다 작다 이동
# step2 5,7은 정렬됨 9가 어디갈지 생각 -> 7보다 크다 다음
# step3 5,7,9는 정렬됨 0이 어디갈지 생각 -> 9보다 작다 이동, 7보다 작다 이동, 5보다 작다 이동
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break # 작은 숫자는 적절한 위치를 찾을때까지 왼쪽으로 이동
            #내림차순으로 되어있으면 가장 오래 걸리겠군

print(array)