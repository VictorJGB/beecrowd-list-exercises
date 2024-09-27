# https://judge.beecrowd.com/pt/problems/view/2399
N = int(input())

mines_array = []
result_array = []

for i in range(N):
    mines_array.append(int(input()))

for i in range(len(mines_array)):
    if i == 0 and len(mines_array) > 1:
        result_array.append(mines_array[i] + mines_array[i + 1])
    elif i == 0:
        result_array.append(mines_array[i])
    elif i == len(mines_array) - 1:
        result_array.append(mines_array[i] + mines_array[i - 1])
    else:
        result_array.append(mines_array[i] + mines_array[i - 1] + mines_array[i + 1])


for result in result_array:
    print(result)
