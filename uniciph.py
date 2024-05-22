import ciphers as c
import english
import english.ic as ic

baseline = "This is a decoded string."
badbaseline = "Lorem ipsum dolor sit amet."
cipherhex = "74 68 69 73 20 69 73 20 68 65 78"
badcipherhex = "74 68 69 73 20 69 73 20 68 65 78 qq"
cipherb64 = "dGhpcyBpcyBiYXNlNjQ="
reversed = "desrever si siht"
rot13 = "Guvf vf n ebg13 pnrfne pvcure"
rot5 = "Ymnx nx f wty5 hfjxfw hnumjw"
rot7 = "Aopz pz h yva7 jhlzhy jpwoly"
rot25 = "Sghr hr z qns25 bzdrzq bhogdq"
sbxor = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
atbash = "Kbgslm Kiltiznnrmt"
bacon = "BAAAB AAAAA BABBA BABAA AABBB AAAAA BAABA"
ictext = "This is an English sentence that I am writing the quick fox jumped over the lazy brown dog."
icparagraph = "If you're looking for random paragraphs, you've come to the right place. When a random word or a random sentence isn't quite enough, the next logical step is to find a random paragraph. We created the Random Paragraph Generator with you in mind. The process is quite simple. Choose the number of random paragraphs you'd like to see and click the button. Your chosen number of paragraphs will instantly appear."
random = "GhFBKrJJxiMXNRCxXiELbhvjFxbwFCLWTyadJeAG"
vigenere = "Dlgc mq k zgqilovc mmnrip gmrr oci OCI"
test = "test"

def testAll(ciphertext):
	c.testHex(ciphertext)
	c.testBase64(ciphertext)
	c.testReverse(ciphertext)
	c.testCaesar(ciphertext)
	c.testSingleByteXOR(ciphertext)
	c.testAtbash(ciphertext)
	ioc = ic.checkIC(ciphertext)
	#hamming = english.checkHamming(ciphertext)

	#print(f'[!] Hamming Distance Test {hamming}')

	if ioc:
		print(f'[!] IC {ioc}')
	else:
		print(f'[!] IC {ioc} | No alpha characters detected')


def main():
	testAll(rot7)

	if not c.matchlist:
		print('No matches found.')
	else:
		print('\n'.join(c.matchlist))

if __name__ == "__main__":
	main()