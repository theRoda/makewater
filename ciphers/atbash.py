import string
import ciphers.check as check

def testAtbash(ciphertext):
	alphabet = string.ascii_lowercase
	reversealpha = str.maketrans(alphabet, alphabet[::-1])
	decoded = ciphertext.lower().translate(reversealpha)
	check.checkMatch(decoded, None, 'Atbash')