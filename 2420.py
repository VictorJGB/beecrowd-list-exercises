# https://judge.beecrowd.com/pt/problems/view/2420
N = int(input())

section_array = list(map(int, input().split()))

section_frontier = 0
counter = 0

target_sum = sum(section_array) / 2

for i in range(N):
    counter += section_array[i]

    if counter >= target_sum:
        section_frontier = i + 1
        break

print(section_frontier)
