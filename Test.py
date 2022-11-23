import XOR-Encoding

#Here we do a quick test

enc = str_xor(message, key)
print('Encrypted messge is: ' + '\n' + enc + '\n')


dec = str_xor(enc, key)
print('Decrypted messge is: ' + '\n' + dec)


assert(dec == "testmessage")
