# https://judge.beecrowd.com/pt/problems/view/1471

while True:
    try:
        N, R = map(int, input().split())
        returned_divers = []
        drowed_divers = []

        # Input de mergulhadores que retornaram
        returned_divers = list(map(int, input().split()))

        for i in range(N):
            if i + 1 not in returned_divers:
                drowed_divers.append(i + 1)

        if len(drowed_divers) > 0:
            print(" ".join(map(str, drowed_divers)) + " ")
        else:
            print("*")
    except EOFError:
        break
