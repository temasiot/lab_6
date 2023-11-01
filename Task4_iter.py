from random import randint


def create(n):
    while True:
        a = []
        for i in range(n):
            a.append(randint(0, 100))
        if a.count(0) >= 2:
            break
    return a


def index_max(a, n):
    q = 0
    for i in range(n):
        if a[i] > q:
            q = a[i]
            e = i
    return e


def find_index_2_zero(a):
    q = a.index(0)
    a[q] = 1
    w = a.index(0)
    a[q] = 0
    return q, w


def sum_by_index(a, q, w):
    e = 0
    for i in range(q+1, w):
        e += a[i]
    return e


def swap_array(arr):
    odd = []
    even = []
    for i in range(len(arr)):
        if i % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    return even + odd


def out(a):
    for i in range(len(a)):
        print('{:>4}'.format(a[i]),end="")
    print()


def main():
    n = int(input('n = '))
    a = create(n)
    print('початковий масив =', end="")
    out(a)
    print('Номер максимального елементу масиву =', index_max(a, n)+1)
    q, w = find_index_2_zero(a)
    print('Добуток елементів між першим і другим нулем =', sum_by_index(a, q, w))
    print('масив після змін =', end="")
    out(swap_array(a))


if __name__ == '__main__':
    main()
