import sys
import time
import argparse
import logging
from logging.handlers import RotatingFileHandler
import ciphers as c
import analysis.ic as ic

logger1 = logging.getLogger(__name__)
logger1.setLevel(logging.DEBUG)
filehandler = RotatingFileHandler('uniciph.log', maxBytes=10*1024*1024, backupCount=10)
screenhandler = logging.StreamHandler(sys.stdout)
screenhandler.setLevel(logging.INFO)
#formatter = logging.Formatter('%(asctime)s UTC - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s UTC - %(levelname)s - %(message)s')
logging.Formatter.converter = time.gmtime
filehandler.setFormatter(formatter)
screenhandler.setFormatter(formatter)
logger1.addHandler(filehandler)
logger1.addHandler(screenhandler)


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
	logcipher = (ciphertext[:68] + '..truncate..') if len(ciphertext) > 68 else ciphertext
	logger1.debug(f'Using ciphertext {logcipher}')
	c.testHex(ciphertext)
	c.testBase64(ciphertext)
	c.testReverse(ciphertext)
	c.testCaesar(ciphertext)
	c.testSingleByteXOR(ciphertext)
	c.testAtbash(ciphertext)
	ioc = ic.checkIC(ciphertext)


	if ioc:
		logger1.info(f'IC {ioc}')
		#print(f'[!] IC {ioc}')
	else:
		logger1.info(f'[!] IC {ioc} | No alpha characters detected')
		#print(f'[!] IC {ioc} | No alpha characters detected')

	if c.isHexString(ciphertext):
		logger1.info(f'[!] Ciphertext is a hex string')
		#print(f'[!] Ciphertext is a hex string')


def main():
	logger1.debug('----------')
	logger1.debug('Starting cracking')
	args = parser.parse_args()
	prefilter = args.prefilter

	if args.ciphertext is not None:
		logger1.debug('Ciphertext supplied as string')
		ciphertext = args.ciphertext
		testAll(ciphertext)
	elif args.file is not None:
		logger1.debug('Ciphertext supplied as file with one cipher')
		with open(args.file, 'r') as filename:
			ciphertext = filename.read()
			if prefilter == 'hex':
				# todo: run checks like isHexString before filtering if prefilter set
				# bundle analysis checks? isBLAH, IC, etc.
				filtered = c.decodeHex(ciphertext)
				testAll(filtered)
			else:
				testAll(ciphertext)
	elif args.manyinfile is not None:
		logger1.debug('Ciphertext supplied as file with multiple ciphers')
		with open(args.manyinfile, 'r') as filename:
			for line in filename:
				ciphertext = line
				testAll(ciphertext)
	else:
		logger1.info('No ciphertexts supplied. Cracking a ciphertext anyway.')
		#print('[!] No ciphertext arguments supplied. Cracking a ciphertext anyway.')
		testAll(sbxor)


	if not c.matchlist:
		logger1.debug('No matches found')
		#print('No matches found.')
	else:
		matches = '\n'.join(c.matchlist)
		logger1.debug('Found match')
		logger1.info(f'{matches}')
		#print(matches)

	logger1.debug('Stopped cracking')

if __name__ == "__main__":
	main()