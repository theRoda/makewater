from collections import Counter
from base64 import b64encode,b64decode

# https://en.wikipedia.org/wiki/Index_of_coincidence
# rkxor yarrr. thanks vij

def checkIC(ciphertext):
    cleantext = ''.join([i.lower() for i in ciphertext if i.isalpha()])
    freq = Counter(cleantext)
    numerator = 0.0
    denominator = 0.0
    for f in freq.values():
        numerator += f * (f - 1)
        denominator += f
    if (denominator == 0.0):
        return(denominator)
    else:
        ic = round(numerator / (denominator * (denominator - 1)), 5)
        return(ic)


def bwxor(s1, s2):
    return bytes([x ^ y for (x, y) in zip(s1, s2)])

# def checkHamming(ciphertext, key):
#     #test = "this is a test"
#     #wokka = "wokka wokka!!!"
#     assert len(ciphertext) == len(key), 'Cannot check hamming distance, lengths do not match'
#     q1 = bytearray.fromhex(ciphertext.encode().hex())
#     q2 = bytearray.fromhex(key.encode().hex())
#     return(sum(bin(byte).count('1') for byte in bwxor(q1, q2)))

def checkHamming(a, b):
    xorbytes = [a[i] ^ b[i] for i, x in enumerate(a)]
    binarybytes = [bin(i)[2:] for i in xorbytes]
    binarystring = ''.join(binarybytes)
    binary = list(map(int, list(binarystring)))
    count = sum(binary)
    return count

def makeChunks(iterable, chunksize):
    chunks = [iterable[i:i + chunksize] for i in range(0, len(iterable), chunksize) if i < len(iterable) - chunksize]
    return(chunks)
def normalizedHamming(ciphertext, keysize):
    assert keysize < len(ciphertext) / 2, 'text is too short to provide two blocks at this key size'
    bytelist = b64decode(ciphertext)
    assert isinstance(bytelist, (bytes, bytearray)), 'hamming distance must be calculated with raw bytes'
    chunks = makeChunks(bytelist, keysize)
    blocks = [bytelist[0:keysize], bytelist[keysize:keysize * 2]]
    hamming = [[checkHamming(block, chunk) for chunk in chunks] for block in blocks][0]
    mean = sum(hamming) / len(hamming)
    normalized = mean / keysize
    return normalized

def smallest(values):
    sortedlowhigh = sorted(values, key=lambda x: x.get('distance'))
    return sortedlowhigh[0].get('keysize')

def findKeySize(text):
    normalizedhammingdist = [
        {
          'keysize': keysize,
          'distance': normalizedHamming(text, keysize)
        }
        for keysize
        in list(range(2, 41))
    ]
    keys = smallest(normalizedhammingdist)
    return keys

def transpose(text, size):
    bytelist = b64decode(text)
    chunks = makeChunks(bytelist, size)
    transposed = list(zip(*chunks))
    assert chunks[0][0] == transposed[0][0], 'matrix transposition failed'
    assert chunks[0][1] == transposed[1][0], 'matrix transposition failed'
    assert chunks[0][2] == transposed[2][0], 'matrix transposition failed'
    return transposed

def singleXOR(bytelist, key):
    return [b ^ key for b in bytelist]

def asciiAll():
    return [chr(x) for x in range(128)]

def detectKey(strings):
    common = list('etaoin shrdlu')
    counts = [
        sum([string.count(character) for character in common])
        for string in strings
    ]
    maximum = max(counts)
    index = counts.index(maximum)
    return chr(index)

def findXORKey(bytelist):
    xorbytes = [singleXOR(bytelist, ord(character)) for character in asciiAll()]
    xorstrings = [''.join(list(map(chr, integer))) for integer in xorbytes]
    key = detectKey(xorstrings)
    return key

def findVigenereKey(text):
    keysize = findKeySize(text)
    transposedbytes = transpose(text, keysize)
    vigenerekey = ''.join([findXORKey(x) for x in transposedbytes])
    return vigenerekey

def decryptVigenere(ciphertext, key):
    bytestext = b64decode(ciphertext)
    byteskey = bytearray.fromhex(key.encode().hex())
    decryptedbytes = [b ^ byteskey[i % len(byteskey)] for i, b in enumerate(bytestext)]
    decryptedchars = [chr(b) for b in decryptedbytes]
    decryptedcipher = ''.join(decryptedchars)
    return decryptedcipher