import unittest
import sys

import correct_function as correct
import encryption as student


p, q = correct.Prime_generation()


class Test_encryption(unittest.TestCase):

    def test(self):
        correct_keys = correct.keys_generation(p, q)
        correct_private_key = correct_keys[0]
        correct_public_key = correct_keys[1]

        try:
            # Génére deux chiffrement, celui de l'étudiant et celui de la correction
            student_rep = student.encryption("test", correct_public_key)
            correct_rep = correct.encryption("test", correct_public_key)

            # Compare les deux chiffrements
            self.assertEqual(student_rep, correct_rep, "The encryption format is incorrect")

        except Exception as err:
               self.fail("Il y a des erreurs  " + str(err) )
                
    # Vérifie si la fonction gére les entrées incorrectes            
    def test_incorrect_input(self):
        try:
            student_rep = student.encryption(-10, "test")
            self.assertIsNone(student_rep, "Votre fonction ne gére pas les entrées incorrectes")

        except Exception as e:
                 self.fail("Votre fonction ne gére pas les entrées incorrectes")


if __name__ == '__main__':
    unittest.main()