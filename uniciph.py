import argparse
import ciphers as c
import analysis.ic as ic

parser = argparse.ArgumentParser(description='Universal Cipher Bruteforce Tool')
inputmethod = parser.add_mutually_exclusive_group()
inputmethod.add_argument('-c', '--ciphertext', type=str, default=None, help='Give the ciphertext as an argument')
inputmethod.add_argument('-f', '--file', type=str, default=None, help='Give the ciphertext as a file. Used for cracking a single piece of text.')
inputmethod.add_argument('-m', '--manyinfile', type=str, default=None, help='Give the ciphertext as a file of newline seperated strings. Used for cracking many ciphertexts in a single file.')
parser.add_argument('-p', '--prefilter', choices=['hex', 'reverse'], default=None, help='Apply a filter before cracking. Current option is "hex".')


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

	if c.isHexString(ciphertext):
		print(f'[!] Ciphertext is a hex string')


def main():
	args = parser.parse_args()
	prefilter = args.prefilter




	if args.ciphertext is not None:
		ciphertext = args.ciphertext
		testAll(ciphertext)
	elif args.file is not None:
		with open(args.file, 'r') as filename:
			ciphertext = filename.read()
			if prefilter == 'hex':
				filtered = c.decodeHex(ciphertext)
				testAll(filtered)
			else:
				testAll(ciphertext)
	elif args.manyinfile is not None:
		with open(args.manyinfile, 'r') as filename:
			for line in filename:
				ciphertext = line
				testAll(ciphertext)
	else:
		print('No ciphertext arguments supplied. Cracking a ciphertext anyway.')
		testAll(sbxor)


	if not c.matchlist:
		print('No matches found.')
	else:
		print('\n'.join(c.matchlist))

if __name__ == "__main__":
	main()