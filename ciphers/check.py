import english as e

matchlist = []
def checkMatch(message, key, cipher):
	cleanmessage = message.strip()
	trimmedmessage = (cleanmessage[:70] + '..truncate..') if len(cleanmessage) > 70 else cleanmessage
	if e.detectenglish.isEnglish(message, 50, 50):
		matchlist.append(f'[!] {trimmedmessage} | {cipher} | Key: {key}')
	else:
		pass