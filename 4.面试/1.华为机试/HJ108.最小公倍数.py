n1 = int(input())
n2 = int(input())


def lcm(n1: int, n2: int):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    while (True):
        if (greater % n1 == 0) and (greater % n2 == 0):
            lcm_1 = greater
            break
        greater += 1
    return lcm_1


print(lcm(n1, n2))
