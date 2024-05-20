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
        print(f'[!] IC: 0 | No alpha characters detected.')
    else:
        ic = round(numerator / (denominator * (denominator - 1)), 5)
        print(f'[!] IC: {ic}')