input = '10 7'
n,find = map(int, input.split())
input = '1 3 5 7 9 11 13 15 17 19'
array = list(map(int, input.split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

idx = binary_search(array, find, 0, n-1)
if idx == None:
    print('찾고자하는 값이 없습니다.')
else:
    print(array[idx],',',idx+1,'번째에 있음')