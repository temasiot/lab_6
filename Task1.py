from random import randint


def decide(q, w, e):
    for i in range(len(q)):
        if q[i] > 0 or q[i] % 3 != 0:
            w = w_sum(q, i, w)
            q = tozero(q, i)
            e = counter(e)
    return q, w, e


def w_sum(q, i, w):
    w += q[i]
    return w


def tozero(q, i):
    q[i] = 0
    return q


def counter(e):
    e += 1
    return e


def out(a):
    for i in range(len(a)):
        print('{:>3}'.format(a[i]),end="")
    print()


def generate(n, a):
    for i in range(n):
        a.append(randint(-10, 35))
    return a


def main():
    a = []
    generate(22, a)
    print('початковий масив =', end="")
    out(a)
    w = 0
    e = 0
    a, w, e = decide(a, w, e)
    print('масив після змін =', end="")
    out(a)
    print('сума =', w)
    print('лічильник =', e)
    pass


if __name__ == '__main__':
    main()
