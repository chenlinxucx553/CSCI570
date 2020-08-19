def gen_prime(num):
    res = set()
    for val in range(1, num + 1):
        if val > 1:
            for i in range(2, val):
                if val % i == 0:
                    break
            else:
                res.add(val)
    print(sorted(list(res)))


def gen2(num):
    res = []
    for i in range(2, num + 1):
        for j in range(2, i + 1):
            if i % j == 0:
                break
        if j == i:  
            res.append(j)
    print(res)


# gen_prime(41)

gen2(41)


def find_all_prime(num):
    res = set()
    for val in range(2, num + 1):
        prime = True
        for y in range(2, val):
            if val % y == 0:
                prime = False
        if prime:
            res.add(val)

    return res
