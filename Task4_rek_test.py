from unittest import TestCase, main
from Task4_rek import swap_array


class Test(TestCase):
    def test_func(self):
        a = [1, 2, 3, 4, 5]
        b = [1, 3, 5, 2, 4]
        s = swap_array(a, [], [], 0)
        self.assertEqual(s[0]+s[1], b)


if __name__ == "__main__":
    main()
