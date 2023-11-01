from unittest import TestCase, main
from Task_1_rek import decide


class Test(TestCase):
    def test_func(self):
        a = [3, 24, -3, -8, -6, 15, 6, 23, 6, -3, 4, 5, -4, 27, 22, 16, 34, 21, 18, 11, 5, 10]
        b = ([0, 0, -3, 0, -6, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 238, 19)
        self.assertEqual(decide(a, 0, 0, 0), b)


if __name__ == "__main__":
    main()
