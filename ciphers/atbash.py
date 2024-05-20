import ciphers.check as check

def testAtbash(ciphertext):
	AtoM = 'ABCDEFGHIJKLM'
	ZtoN = 'ZYXWVUTSRQPON'
	decoded = ''
	for c in ciphertext.upper():
		if c.isalpha():
			num = AtoM.find(c) if c in AtoM else ZtoN.find(c)
			decoded += ZtoN[num] if c in AtoM else AtoM[num]
		else:
			decoded += c
	check.checkMatch(decoded, None, 'Atbash')