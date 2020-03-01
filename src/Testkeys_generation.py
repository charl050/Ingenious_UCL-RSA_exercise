#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import Corrkeys_generation as correct
import keys_generation as student


class Test_keys_generation(unittest.TestCase):

    def test_length(self):
        args = [3,5,4]
        for n in args:
            try:
                student_rep = student.keys_generation(n)
            except Exception as e:
                self.fail("Echec")
            self.assertEqual(len(str(student_rep[0][2])), n)
            
    def test_invalid_input(self):
            args = [-3,0,'test']
            for n in args:
                try:
                    student_rep = student.keys_generation(n)
                except Exception as e:
                    self.fail("Echec")
                self.assertIsNone(student_rep)
        
        


if __name__ == '__main__':
    unittest.main()
