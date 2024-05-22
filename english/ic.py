from collections import Counter

# https://en.wikipedia.org/wiki/Index_of_coincidence

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

def checkHamming(ciphertext):
    test = "this is a test"
    wokka = "wokka wokka!!!"
    q1 = bytearray.fromhex(test.encode('utf-8').hex())
    q2 = bytearray.fromhex(wokka.encode('utf-8').hex())
    return(sum(bin(byte).count('1') for byte in bwxor(q1, q2)))