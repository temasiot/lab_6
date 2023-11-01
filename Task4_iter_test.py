from unittest import TestCase, main
from Task4_iter import swap_array


class Test(TestCase):
    def test_func(self):
        a = [1, 2, 3, 4, 5]
        b = [1, 3, 5, 2, 4]
        self.assertEqual(swap_array(a), b)


if __name__ == "__main__":
    main()
