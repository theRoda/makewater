# makewater
decrypt things

Credit to http://inventwithpython.com/hacking for the english detection ideas.
<br><br>
*usage: python makewater.py --help*
<br><br>
* Current features:
  * Brute force
    * Base64
    * Reverse
    * Atbash
    * Caesar
    * Hex
    * Single byte XOR
    * Hex Prefilter
    * Repeating key XOR
  * Analysis
    * IC
    * Hammming Distance
    * String Encoding Detection: Hex
    * String Encoding Detection: Base64


* Roadmap:
  * take key(s) as argument
  * take key(s) file as argument
  * runtime argument to set min letters and words in detectEnglish
  * cipher identification
  * railfence 
  * baconian
  * affine
  * transposition
  * bifid
  * columnar transposition
  * double transposition
  * playfair
  * Übchi
  * vigenere
  * frequency analysis
  * Cohen's kappa test
  * Chi test
  * general performance improvements
  * more strings encoding detection
<br><br>
note: When using newDetectEnglish(), the default is to require 60% words and 75% letters to return a match. The ideal values can vary greatly depending on plaintext length and contents. These values can be tweaked in the isEnglish() function, or when calling isEnglish() eg. `isEnglish(cleartext, 50, 80)` would require 50% words and 80% letters.
