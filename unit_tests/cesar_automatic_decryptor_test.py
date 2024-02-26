import unittest
from cesar_automatic_decryptor import ceasar_brute_force

class TestCeasarAutomaticDecryptor(unittest.TestCase):

    def test_ceasar_brute_force(self):

        expected_decrypted_sentence = "the quick brown fox jumps over the lazy dogs"
        self.assertEqual(ceasar_brute_force("gur dhvpx oebja sbk whzcf bire gur ynml qbtf"), expected_decrypted_sentence)

        expected_decrypted_sentence = "this is just a sentence"
        self.assertEqual(ceasar_brute_force("aopz pz qbza h zlualujl"), expected_decrypted_sentence)

        expected_decrypted_sentence = "word home notebook"
        self.assertEqual(ceasar_brute_force("dvyk ovtl uvalivvr"), expected_decrypted_sentence)

        self.assertIsNone(ceasar_brute_force("dwqevyk ovwerrwtl uvalwivvr"))

    def test_ceasar_brute_force_empty_sentence(self):
        expected_decrypted_sentence = None    
        decrypted_sentence = ceasar_brute_force("")
    
        self.assertEqual(decrypted_sentence, expected_decrypted_sentence)

if __name__ == '__main__':
    unittest.main()
