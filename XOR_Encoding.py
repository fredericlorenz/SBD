import string # The random and string libraries are used to generate a random string with flexible criteria
import random


class Encrypter:
	@staticmethod
	def str_xor(s1, s2):
		return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])
	
	@staticmethod
	def gen_key():
		key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(1024))
		return key
