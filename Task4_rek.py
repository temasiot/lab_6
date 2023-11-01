from random import randint


def create(n):
    a = generate(n, list(), 0)
    if a.count(0) < 2:
        a = create(n)
    return a


def generate(n, a, i):
    a.append(randint(0, 100))
    if i < n - 1:
        a = generate(n, a, i + 1)
    return a


def index_max(a, n, i, q, e):
    if a[i] > q:
        q = a[i]
        e = i
    if i < n - 1:
        e = index_max(a, n, i+1, q, e)
    return e


def find_index_2_zero(a):
    q = a.index(0)
    a[q] = 1
    w = a.index(0)
    a[q] = 0
    return q, w


def sum_by_index(a, i, w, e):
    e += a[i]
    if i < w - 1:
        e = sum_by_index(a, i+1, w, e)
    return e


def swap_array(arr, odd, even, i):
    if i % 2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
    if i < len(arr) - 1:
        even, odd = map(list,swap_array(arr, odd, even, i+1))
    return even, odd


def out(a, i):
    print('{:>4}'.format(a[i]),end="")
    if i < len(a) - 1:
        out(a, i+1)
    else:
        print()


def main():
    n = int(input('n = '))
    a = create(n)
    print('початковий масив =', end="")
    out(a, 0)
    print('Номер максимального елементу масиву =',index_max(a, n, 0, 0, 0)+1)
    q, w = find_index_2_zero(a)
    print('Добуток елементів між першим і другим нулем =',sum_by_index(a, q+1, w, 0))
    s = swap_array(a, [], [], 0)
    print('масив після змін =', end="")
    out(s[0]+s[1], 0)


if __name__ == '__main__':
    main()
