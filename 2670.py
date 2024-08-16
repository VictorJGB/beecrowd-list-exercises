# https://judge.beecrowd.com/pt/problems/view/2670

A1 = int(input())
A2 = int(input())
A3 = int(input())

sol1 = A2 * 2 + A3 * 4
sol2 = A1 * 2 + A3 * 2
sol3 = A1 * 4 + A2 * 2

print(min(min(sol1, sol2), sol3))