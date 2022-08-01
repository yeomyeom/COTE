# 기준 데이터를 정하고 그 기준보다 작은 데이터와 큰 데이터의 위치를 서로 바꾸면 어떨까?
# 퀵정렬
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array:list[int], start:int, end:int) -> list[int]:
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # pivot 보다 큰 애를 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot 보다 작은 애 찾기
        while right >= start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            # 엇갈렸다면 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array,0,len(array)-1)
print(array)
