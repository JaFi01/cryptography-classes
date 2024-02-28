import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

#nltk.download()

def check_word_sense(word: str):
    if wordnet.synsets(word):
        return True
    else:
        return False


def vigenere_brute_force(ciphertext: str):
    """Brutforce through ciphertext, and counting valid words in each decryption iteration

    Args:
        ciphertext (str): encrypted sentence or words in english

    Returns:
        str: most propable decrypted sentence (most of words after decryption exists)
    """
    ALPHABET_SIZE = 26
    max_valid_count = 0
    best_shift = None
    best_decrypted_text = None
    
    for shift1 in range(0, ALPHABET_SIZE):
        for shift2 in range(0, ALPHABET_SIZE):
            for shift3 in range(0, ALPHABET_SIZE):
                decrypted_text = ''
                decrypted_text_tokens = ''
                i=0
                for char in ciphertext:
                    if char.isalpha():
                        if i % 3 == 0:
                            shift = shift1
                        elif i % 3 == 1:
                            shift = shift2
                        else:
                            shift = shift3
                        i += 1
                        if(char.isupper()):
                            char = ord(char) + 32
                        if char.islower():
                            position = ord(char) - ord('a')
                            new_position = (position - shift) % ALPHABET_SIZE
                            decrypted_text += chr(new_position + ord('a'))
                    else:
                        decrypted_text += char
                    
                    decrypted_text_tokens = word_tokenize(decrypted_text)
                
                valid_count = 0
                if decrypted_text_tokens is not None:
                    for token in decrypted_text_tokens:
                        if check_word_sense(token):
                            valid_count += 1
                #checking if tested sentence is one making most sense (has most valid words)
                if valid_count > max_valid_count:
                    max_valid_count = valid_count
                    best_shift = (shift1, shift2, shift3)
                    best_decrypted_text = decrypted_text_tokens
                    print (decrypted_text_tokens, valid_count, best_shift)
            
    if best_shift is not None:
        return ' '.join(best_decrypted_text)
    else:
        return None