from XOR_Encoder import Encrypter

message = "Test"
key = Encrypter.gen_key()
enc = Encrypter.str_xor(message, key)
dec = Encrypter.str_xor(enc, key)

assert(dec == message)
