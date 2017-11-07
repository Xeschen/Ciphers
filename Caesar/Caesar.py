import sys

def Caesar(filepath, key):
	file = open(filepath)
	message = []
	for line in file:
		message.append(list(line))
	file.close()

	cipher = []

	for m in message:
		cline = []
		for word in m:
			trans = ord(word)
			if (ord('A')<ord(word) and ord('Z')>ord(word)) or (ord('a')<ord(word) and ord('z')>ord(word)):
				trans = ord(word) + key
				if trans > ord('z') or (ord(word) < ord('Z') and trans > ord('Z')):
					trans -= 26
			cline.append(chr(trans))
		cipher.append(''.join(cline))
	return cipher
	
if __name__ == "__main__":
	FILEPATH = 'message.txt'
	KEY = 3
	cipher = Caesar(FILEPATH, KEY)
	print(cipher)