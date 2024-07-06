#encryption and decryption tool using Caesar cipher algorithm

def caesar_cipher(text, shift):
    result=""
    for char in text:
        if char.isalpha():
            shifted=ord(char) + shift

            if char.isupper():
                if shifted > ord('Z'):
                    shifted-=26
                elif shifted < ord("A"):
                    shifted += 26
        
            elif char.islower():
                if shifted > ord("z"):
                    shifted-=26
                elif shifted < ord("a"):
                    shifted += 26
            result +=chr(shifted)

        else:
            result +=char
    return result


def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

text= input("Enter a message:")
shift= int(input("enter a shift value:"))

encrypted_text= caesar_cipher(text, shift)
print("Encrypted:", encrypted_text)

decrypted_text=caesar_decipher(encrypted_text, shift)
print("Decrypted:", decrypted_text)
