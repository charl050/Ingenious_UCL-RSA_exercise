import unittest
import sys

import correct_function as correct
import decrypt as student


p, q = correct.Prime_generation()

class Test_decryption(unittest.TestCase):

    def test(self):
        # Génère  les clés publiques et privées utilisé pour la correction
        correct_keys = correct.keys_generation(p, q)
        correct_private_key = correct_keys[0]
        correct_public_key = correct_keys[1]

        # Génére un chiffrement
        correct_encryption = correct.encryption("test", correct_public_key)
        correct_decryption = correct.decrypt(correct_encryption, correct_private_key)

        try:
            # Génére les déchiffrements de l'étudiant et de la correction pour les comparer
            student_rep = student.decrypt(correct_encryption, correct_private_key)
            correct_rep = correct.decrypt(correct_encryption, correct_private_key)

            # Comparer les deux déchiffrements
            self.assertEqual(student_rep, correct_rep, "La fonction de déchiffrement ne fonctionne pas correctement")

        except Exception as e:
                self.fail("Il y a des erreurs :  " + str(e))
                
    # Vérifie si la fonction gére les entrées incorrectes              
    def test_incorrect_input(self):
        try:
            student_rep = student.decrypt(-10, "test")
            self.assertIsNone(student_rep, "Votre fonction ne gére pas les entrées incorrectes")

        except Exception as e:
                 self.fail("Votre fonction ne gére pas les entrées incorrectes")            



if __name__ == '__main__':
    unittest.main()
