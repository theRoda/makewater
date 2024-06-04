import base64
import ciphers.check as check

def testBase64(ciphertext):
    try:
        decoded = base64.b64decode(ciphertext)
        decodedstring = decoded.decode("utf-8")
        check.checkMatch(decodedstring, None, 'Base64')
    except:
        pass

def isBase64String(ciphertext):
    try:
        return base64.b64encode(base64.b64decode(ciphertext)).decode() == ciphertext
    except:
        return False