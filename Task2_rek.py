from random import randint


def min_nepar(q, w):
    if min(q) % 2 != 0:
        return q, q.index(min(q))
    else:
        q[q.index(min(q))] = max(q)+1
    if w < len(q)-1:
        q, e = min_nepar(q, w+1)
    else:
        return q, -1
    return q, e


def generate(n, a, i):
    a.append(randint(0, 100))
    if i < n - 1:
        a = generate(n, a, i + 1)
    return a


def out(a, i):
    print('{:>4}'.format(a[i]),end="")
    if i < len(a) - 1:
        out(a, i+1)
    else:
        print()


def main():
    n = int(input('n = '))
    a = generate(n, [], 0)
    print('початковий масив =', end="")
    out(a, 0)
    a, p = min_nepar(a, 0)
    if p != -1:
        print('масив після змін =', end="")
        out(a, 0)
        print('індекс =', p)
    else:
        print('всі елементи парні')
    pass


if __name__ == '__main__':
    main()
