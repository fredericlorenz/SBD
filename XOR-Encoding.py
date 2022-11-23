import string # The random and string libraries are used to generate a random string with flexible criteria
import random
# XOR Encryption

# Random Key Generator
key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(1024))

print(key)
print('\n' + 'Key length = ' + str (  len(key) ))


message = 'testmessage'  # this is the message which we will encrypt before it's getting sent
print("Msg is " + message + '\n')


def str_xor(s1, s2):
 return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])



#Here we do a quick test

enc = str_xor(message, key)
print('Encrypted messge is: ' + '\n' + enc + '\n')


dec = str_xor(enc, key)
print('Decrypted messge is: ' + '\n' + dec)


assert(dec == "testmessage")




#Here we do a quick test 

enc = str_xor(message, key)
print 'Encrypted messge is: ' + '\n' + enc + '\n' 


dec = str_xor(enc, key)
print 'Decrypted messge is: ' + '\n' + dec

#Make sure that the SAME Key is HARDCODED in the Server AND client, ohterwise you won't be able to decode your own messages!
