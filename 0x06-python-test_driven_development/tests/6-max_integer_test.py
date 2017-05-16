#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

        def test_int_max(self):
                self.assertEqual(max_integer([3, 4, 5, 6]), 6)

        def test_none_max(self):
                self.assertIsNone(max_integer())

        @unittest.expectedFailure
        def test_is_int(self):
                self.assertEqual(max_integer("Guillaume"), "nope")

        @unittest.expectedFailure
        def test_not_int(self):
                self.assertEqual(max_integer([1, 2, 3, "julien"]), "nope")

        @unittest.expectedFailure
        def test_str_in_list(self):
                self.assertEqual(max_integer([a, 1, 2, 4]), "nope")

        def test_negative_list(self):
                self.assertEqual(max_integer([-1, 4, 6]), 6)

        @unittest.expectedFailure
        def test_float_in_list(self):
                self.assertEqual(max_integer([4.5, 6.9]), "nope")

        @unittest.expectedFailure
        def test_float(self):
                self.assertEqual(max_integer(4.5), "nope")

        def test_all_negative_list(self):
                self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        @unittest.expectedFailure
        def test_none_in_list(self):
                self.assertIsNone(max_integer([None, 1, 2]))

        def test_just_none_in_list(self):
                self.assertIsNone(max_integer([None]), None)

        def test_with_boolean(self):
                self.assertEqual(max_integer([True, False, 1, 2, 3]), 3)

        def test_with_big_number(self):
                big_num = 1000000000000000000000000000000000000000001
                self.assertEqual(max_integer([big_num, 3]),
                                 1000000000000000000000000000000000000000001)

        @unittest.expectedFailure
        def test_with_list_none(self):
                self.assertEqual(max_integer([None, None, None]), "nope")

        def test_negative_boolean_list(self):
                self.assertEqual(max_integer([-True, -False, 1, 2]), 2)

        @unittest.expectedFailure
        def test_negative_outside(self):
                self.assertEqual(max_integer(-[1, 2, 3]), "nope")

        @unittest.expectedFailure
        def test_mixed_list_char(self):
                self.assertEqual(max_integer(["g", 1, 2, 4]), "nope")

        def test_empty_list(self):
                self.assertIsNone(max_integer([]))

        @unittest.expectedFailure
        def test_just_boolean(self):
                self.assertEqual(max_integer(True), "nope")

        @unittest.expectedFailure
        def test_just_int(self):
                self.assertEqual(max_integer(2), "nope")

        @unittest.expectedFailure
        def test_too_many_args(self):
                self.assertEqual(max_integer([4, 5], [5, 6]), "nope")

        def test_neg_neg_in_list(self):
                self.assertEqual(max_integer([-54152352152, --43214]), 43214)

        def test_neg_zero(self):
                self.assertEqual(max_integer([--0, -4]), 0)

        def test_neg_boolean(self):
                self.assertEqual(max_integer([--True, -4]), 1)

        def test_neg_pos_number(self):
                self.assertEqual(max_integer([--True, -+4]), 1)

        def test_pos_number(self):
                self.assertEqual(max_integer([--True, +4]), 4)
if __name__ == '__main__':
    unittest.main()
