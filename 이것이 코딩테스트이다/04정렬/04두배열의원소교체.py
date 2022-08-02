input ='5 3'
n,k=map(int,input.split())
input = '1 2 5 4 3'
#a_array = []
a_array = list(map(int, input.split()))
input = '5 5 6 6 5'
#b_array = []
b_array = list(map(int, input.split()))
# 최대 k번 바꿔서 a가 최대 값이 될 수 있도록 
# a_array에 가장 작은 숫자 k개 b_array에 큰 숫자 k개 선택해서 교체

a_array.sort()
b_array.sort(reverse=True)

for i in range(k):
    a_array[i], b_array[i] = b_array[i], a_array[i]

print(sum(a_array))
# 26