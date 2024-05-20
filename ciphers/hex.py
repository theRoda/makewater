import string
import ciphers.check as check


def cleanHex(ciphertext):
    return (ciphertext.replace(' ', '').replace('0x', '').replace(':', '').replace('\\x', '').strip())

def testHex(ciphertext):
    cleancipher = cleanHex(ciphertext)
    if all(h in string.hexdigits for h in cleancipher):
        try:
            decoded = bytearray.fromhex(cleancipher).decode()
            check.checkMatch(decoded, None, 'Hexadecimal')
        except:
            pass
    else:
        pass