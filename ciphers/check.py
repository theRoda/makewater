import english as e

matchlist = []
def checkMatch(message, key, cipher):
	message = message.strip()
	if e.detectenglish.isEnglish(message, 50, 50):
		matchlist.append(f'[!] {message} | {cipher} | Key: {key}')
	else:
		pass