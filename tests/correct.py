import unittest
from main import CryptoWrapper

class Test3DESCorrect(unittest.TestCase):
    def setUp(self):
        self.key = bytes.fromhex('0123456789ABCDEFF0E1D2C3B4A596870123456789ABCDEF')
        self.iv = bytes.fromhex('1234567890ABCDEF')
        self.plaintext = bytes.fromhex('6BC1BEE22E409F96')
        self.expected_ciphertext = bytes.fromhex('4b5f6d4917012a0f')

    def test_pycryptodome_encryption(self):
        result = CryptoWrapper.encrypt_pycryptodome(self.key, self.iv, self.plaintext)
        self.assertEqual(result.hex().lower(), self.expected_ciphertext.hex().lower())

    def test_cryptography_encryption(self):
        result = CryptoWrapper.encrypt_cryptography(self.key, self.iv, self.plaintext)
        self.assertEqual(result.hex().lower(), self.expected_ciphertext.hex().lower())

if __name__ == '__main__':
    unittest.main()