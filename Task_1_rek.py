from random import randint


def decide(q, w, e, i):
    if q[i] > 0 or q[i] % 3 != 0:
        w = w_sum(q, i, w)
        q = tozero(q, i)
        e = counter(e)
    if i < len(q)-1:
        q, w, e = decide(q, w, e, i+1)
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


def generate(n, a, i):
    a.append(randint(-10, 35))
    if i < n - 1:
        a = generate(n, a, i + 1)
    return a


def out(a, i):
    print('{:>3}'.format(a[i]),end="")
    if i < len(a) - 1:
        out(a, i+1)
    else:
        print()


def main():
    a = generate(22, [], 0)
    print('початковий масив =', end="")
    out(a, 0)
    w = 0
    e = 0
    a, w, e = decide(a, w, e, 0)
    print('масив після змін =', end="")
    out(a, 0)
    print('сума =', w)
    print('лічильник =', e)
    pass


if __name__ == '__main__':
    main()
