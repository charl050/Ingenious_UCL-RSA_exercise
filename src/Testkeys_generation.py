import unittest
import sys
import math
import correct_function as correct
import keys_generation as student

# Génére deux nombres premiers
p, q = correct.Prime_generation() 


class Test_keys_generation(unittest.TestCase):

    def test(self):
        # Génére les clés privées et publiques correctes
        correct_rep = correct.keys_generation(p, q)
        try:
            # Génére les clés privées et publiques ainsi que le nombre et et n de l'étudiant
            student_rep = student.keys_generation(p, q)
            public_key_student = student_rep[1]
            e_student = student_rep[1][1]
            n_student = student_rep[1][0]

            # Vérifie si e est premier avec (p-1)*(q-1)
            self.assertEqual(math.gcd(e_student,(p-1)*(q-1)), 1, "e n'est pas premier (p-1)*(q-1)")

            # Vérifie si n est égal à p*q
            self.assertEqual(n_student, p*q, "n n'est pas égal à p*q")

            # Vérifie si la sortie est bien un couple de deux éléments
            self.assertEqual(len(student_rep), 2, "La sortie n'a pas le format attendu")

            # Vérifie si la clé privée à bien 3 composantes
            self.assertEqual(len(student_rep[0]), 3, "La sortie n'a pas le format attendu")

            # Vérifie si la clé publique à bien 2 composantes
            self.assertEqual(len(public_key_student), 2, "La sortie n'a pas le format attendu")

        # Si jamais il y a une erreurs dans la fonction autre que celles au dessus 
        except Exception as err:
                self.fail("Il y a des erreurs " + str(err))

    # Vérifie si la fonction gére les entrées incorrectes            
    def test_incorrect_input(self):
        try:
            student_rep = student.keys_generation(-10, "test")
            self.assertIsNone(student_rep, "Votre fonction ne gére pas les entrées incorrectes")

        except Exception as e:
                 self.fail("Votre fonction ne gére pas les entrées incorrectes")

if __name__ == '__main__':
    unittest.main()
