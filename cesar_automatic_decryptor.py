import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

#nltk.download()

def check_word_sense(word: str):
    if wordnet.synsets(word):
        return True
    else:
        return False


def ceasar_brute_force(ciphertext: str):
    """Brutforce through ciphertext, and counting valid words in each decryption iteration

    Args:
        ciphertext (str): encrypted sentence or words in english
    """
    ALPHABET_SIZE = 26
    max_valid_count = 0
    best_shift = None
    best_decrypted_text = None
    
    for shift in range(1, ALPHABET_SIZE):
        decrypted_text = ''
        valid_count = 0
        
        for char in ciphertext:
            if(char.isupper):
                char = ord(char) + 32
            if (char.islower):
                position = ord(char) - ord('a')
                new_position = (position - shift) % ALPHABET_SIZE
                decrypted_text += chr(new_position + ord('a'))
            else:
                decrypted_text += char
        
        decrypted_text_tokens = word_tokenize(decrypted_text)
        
        for token in decrypted_text_tokens:
            if check_word_sense(token):
                valid_count += 1
        #checking if tested sentence is one making most sense (has most valid words)
        if valid_count > max_valid_count:
            max_valid_count = valid_count
            best_shift = shift
            best_decrypted_text = decrypted_text_tokens
    
    if best_shift is not None:
        print(f"Decrypted sentence: {' '.join(best_decrypted_text)} Most propable shift {best_shift}")
    else:
        print(f"This sentence can't be decrypted:{ciphertext}. Can't find human readable words")

#Test calls
ciphertext = "gur dhvpx oebja sbk whzcf bire gur ynml qbtf"
ceasar_brute_force(ciphertext)
ciphertext = "aopz pz qbza h zlualujl"
ceasar_brute_force(ciphertext)
ciphertext = "dvyk ovtl uvalivvr"
ciphertext = "dwqevyk ovwerrwtl uvalwivvr"
ceasar_brute_force(ciphertext)

#pip install nltk
# TODO: add nltk to requirements.txt
# TODO: separate unit test file