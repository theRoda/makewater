import string
import ciphers.check as check


def cleanHex(ciphertext):
    return (ciphertext.replace(' ', '').replace('0x', '').replace(':', '').replace('\\x', '').strip())

def isHexString(ciphertext):
    cleancipher = cleanHex(ciphertext)
    return(all(h in string.hexdigits for h in cleancipher))


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

def decodeHex(ciphertext):
    cleancipher = cleanHex(ciphertext)
    decoded = ''.join(chr(int(cleancipher[i:i + 2], 16)) for i in range(0, len(cleancipher), 2))
    return(decoded)

