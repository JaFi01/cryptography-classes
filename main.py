from caesar_automatic_decryptor import ceasar_brute_force
from vigenere_automatic_decryptor import vigenere_brute_force

if __name__ == '__main__':
   while True:
        print("Choose decryption method:")
        print("1. Caesar")
        print("2. Vigenère")
        choice = input("Choose (1 or 2): ")
        
        if choice == '1':
            ciphertext = input("Enter the encrypted sentence for decryption using the Caesar cipher: ")
            decrypted_text = ceasar_brute_force(ciphertext)
            if decrypted_text is not None:
                print("Decrypted sentence:")
                print(decrypted_text)
            else:
                print("The program was unable to decipher the sentence.")
            break
        elif choice == '2':
            ciphertext = input("Enter the encrypted sentence for decryption using the  Vigenère'a cipher: ")
            decrypted_text, _ = vigenere_brute_force(ciphertext)
            if decrypted_text is not None:
                print("Decrypted sentence:")
                print(decrypted_text)
            else:
                print("The program was unable to decipher the sentence.")
            break
        else:
            print("Wrong input. Choose 1 or 2.")