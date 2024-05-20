import string
import ciphers.check as check

def testCaesar(ciphertext):
    for rot in range(1,26):
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[rot:] + alphabet[:rot]
        table = str.maketrans(alphabet, shifted_alphabet)
        decoded = ciphertext.lower().translate(table)
        check.checkMatch(decoded, rot, 'Caesar')