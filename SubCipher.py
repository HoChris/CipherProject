import base64
import hashlib
import sys

class SubCipher:

	def __init__(self):
		self.key = ''
		self.encryption = ''
		self.decryption = ''

# encryption key which could be anything
#KEY = b'h6C":w5X;n8DLh?D'

# create a list of all the characters in base64 w/padding
	b64_chars = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=']


	def convert(self, string, type):
		# take a sha512 has of the key
		hash = hashlib.sha512(self.key).hexdigest()

		# initial cipher is a copy of the base 64 characters
		cipher = b64_chars[:]

		# loop over each element in the hash and rearrange the cipher
		for c in hash:
			char_int = int(c,16)
			pos = 65 * (char_int / 15)

			# move the element to the beginning of the list and revers the list
			cipher.insert(0, cipher.pop(int(pos)-1))
			cipher = cipher[::-1]

		subBox = {}

		# create the mapping between base64 characters and the rearranged base 64 characters
		for i, c in enumerate(b64_chars):
			subBox[c] = cipher[i]

		# check if operation is a decryption, key/values must be reversed
		if type == 'd':
			subBox = dict((v,k) for k, v in subBox.items())

		#substitute characters in the string according to the subBox
		for i, c in enumerate(string):
			string[i] = subBox[c]

		return ''.join(string) 


	# base64 endcode plaintext and convert to list of characters
	def encrypt(self, string):
		msgEnc = [c for c in base64.b64encode(string.encode()).decode()]

		return self.convert(msgEnc, 'e')

	def decrypt(self, string):
		msgDec = [c for c in string.strip()]

		return base64.b64decode(convert(msgDec, 'd')).decode()

# subC = SubCipher()

# if sys.argv[1] == '-e':
# 	print(subC.encrypt(sys.stdin.read()))
# if sys.argv[1] == '-d':
# 	print(subC.decrypt(sys.stdin.read()))
