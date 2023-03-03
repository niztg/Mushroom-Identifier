'''
Password encryption
'''

#from cryptography.fernet import Fernet
# from classes import Account
import hashlib

# written by: khalid

#class Password(Account):
    #def encrypt(self):
        #key = Fernet.generate_key()
        #ciphered_text = Fernet(key).encrypt(Account._password)

class Password:
    def __init__(self, hash_algorithm = 'sha512'):
        self.hash_algorithm = hash_algorithm
        
    def hashing(self, password):
        bytes = password.encode('utf-8')
        
        bytes_hashed = hashlib.new(self.hash_algorithm,bytes).digest()
        
        return(bytes_hashed.hex())
        