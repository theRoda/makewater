import ciphers.check as check

def testReverse(ciphertext):
    decoded = ciphertext[::-1]
    check.checkMatch(decoded, None, 'Reverse')