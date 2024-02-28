#ciphertext = "gun fgav gulsho gixyl"
#ciphertext = "ans zzfp zzflmi znrrq"

import unittest
from vigenere_automatic_decryptor import vigenere_brute_force
class TestVigenerereAutomaticDecryptor(unittest.TestCase):
    def test_vigenere_brute_force(self):

        excepted_decrypted_sentence = "dog cats animal shelter"

        self.assertEqual(vigenere_brute_force("ans zzfp zzflmi rtbkfbq"), excepted_decrypted_sentence)
        self.assertEqual(vigenere_brute_force("qbt pngf navzny furygre"), excepted_decrypted_sentence)

        excepted_decrypted_sentence="this is just another test"
        self.assertEqual(vigenere_brute_force("ghhf ir wurg ambtgrr srss"), excepted_decrypted_sentence)
        self.assertIsNone(vigenere_brute_force("qhzteryrtye yruweyrui nahyyweryey"))

    def test_ceasar_brute_force_empty_sentence(self):
        excepted_decrypted_sentence = None
        decrypted_sentence = vigenere_brute_force("")

        self.assertEqual(decrypted_sentence, excepted_decrypted_sentence)

if __name__ == '__main__':
    unittest.main()