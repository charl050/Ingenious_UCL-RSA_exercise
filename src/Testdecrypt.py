#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import encryption
import keys_generation
import decrypt as student


class Test_decrypt(unittest.TestCase):

    def test_all(self):
        args = ["bonjour", "abc", "test"]
        rep = _("Votre fonction renvoie {} au lieu de {}")
        try:
            for n in args:
                private_key, public_key = keys_generation.keys_generation(5)
                encrypted_message = encryption.encryption(n, public_key)
                student_ans = student.decrypt(encrypted_message, private_key)
                self.assertEqual(student_ans, n,rep.format(student_ans,n))
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
    
if __name__ == '__main__':
    unittest.main()