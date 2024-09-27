while True:
    n = int(input())
    if n == 0:
        break
    cartas = []
    for _ in range(n):
        cartas.append(input())
    while len(cartas) > 1:
        cartas.pop(1)
    print(cartas[0])
