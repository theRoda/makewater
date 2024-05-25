# single byte xor
import ciphers.check as check
from analysis import findVigenereKey as fvk
from analysis import decryptVigenere as dv

def testSingleByteXOR(ciphertext):
    for byte in range(256):  # XOR against all possible single hex bytes
        key = bytes([byte])
        try:
            decoded = bytes(x ^ y for x, y in zip(bytes.fromhex(ciphertext), key * len(ciphertext))).decode('utf-8')
            check.checkMatch(decoded, key.hex(), 'Single Byte XOR')
        except:
            pass

def testRepeatingKeyXOR(ciphertext):
    try:
        key = fvk(ciphertext)
        decrypted = dv(ciphertext, key)
        check.checkMatch(decrypted, key, 'Repeating Key XOR')
    except:
        pass

