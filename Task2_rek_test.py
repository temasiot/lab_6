from unittest import TestCase, main
from Task2_rek import min_nepar


class Test(TestCase):
    def test_func(self):
        a = [5, 2, 3, 1, 4]
        b = ([5, 2, 3, 1, 4], 3)
        self.assertEqual(min_nepar(a, 0), b)


if __name__ == "__main__":
    main()
