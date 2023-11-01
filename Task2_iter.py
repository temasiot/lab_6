from random import randint


def min_nepar(q):
    for i in range(len(q)):
        if min(q) % 2 != 0:
            return q, q.index(min(q))
        else:
            q[q.index(min(q))] = max(q)+1
    return q, -1


def generate(n, a):
    for i in range(n):
        a.append(randint(0, 100))
    return a


def out(a):
    for i in range(len(a)):
        print('{:>4}'.format(a[i]),end="")
    print()


def main():
    n = int(input('n = '))
    a = []
    a = generate(n, a)
    print('початковий масив =', end="")
    out(a)
    a, p = min_nepar(a)
    if p != -1:
        print('масив після змін =', end="")
        out(a)
        print('індекс =',p)
    else:
        print('всі елементи парні')
    pass


if __name__ == '__main__':
    main()
