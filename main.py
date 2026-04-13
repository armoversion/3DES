from Crypto.Cipher import DES3
from cryptography.hazmat.decrepit.ciphers.algorithms import TripleDES
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.backends import default_backend

class CryptoWrapper:
    @staticmethod
    def encrypt_pycryptodome(key, iv, plaintext):
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        return cipher.encrypt(plaintext)

    @staticmethod
    def encrypt_cryptography(key, iv, plaintext):
        cipher = Cipher(TripleDES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        return encryptor.update(plaintext) + encryptor.finalize()