#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import Correncryption as correct
import encryption as student


class Test_encrypt(unittest.TestCase):

    def test_invalid_input(self):
        args = [(124444,[5352, 32114]), ("bonjour",["test", "test"])]
        for n in args:
            a, b = n
            try:
                student_rep = student.encryption(a,b)
            except Exception as e:
                self.fail()
            self.assertIsNone(student_rep)


if __name__ == '__main__':
    unittest.main()