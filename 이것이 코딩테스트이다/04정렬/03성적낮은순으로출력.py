input = '4'
n = input
array = []
input = '홍길동 95'
array.append((input.split()[0], input.split()[1]))
input = '홍길일 100'
array.append((input.split()[0], input.split()[1]))
input = '홍길삼 77'
array.append((input.split()[0], input.split()[1]))
input = '홍길이 70'
array.append((input.split()[0], input.split()[1]))

array = sorted(array, key=lambda x: x[1])

for result in array:
    print(result[0])