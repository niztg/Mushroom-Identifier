#from cryptography.fernet import Fernet
import hashlib
from classes import Account

#class Password(Account):
    #def encrypt(self):
        #key = Fernet.generate_key()
        #ciphered_text = Fernet(key).encrypt(Account._password)

class Password:
    def __init__(self, hashAlgorithm = 'sha512'):
        self.hashAlgorithm = hashAlgorithm
        
    def hashing(self, Account._password):
        bytes = Account._password.encode('utf-8')
        
        bytes_hashed = hashlib.new(self.algorithm,bytes).digest()
        
        return(password_hashed = bytes_hashed.hex())
        