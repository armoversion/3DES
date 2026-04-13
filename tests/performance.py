import time
import unittest
from main import CryptoWrapper

class Test3DESPerformance(unittest.TestCase):
    def setUp(self):
        self.key = bytes.fromhex('0123456789ABCDEFF0E1D2C3B4A596870123456789ABCDEF')
        self.iv = bytes.fromhex('1234567890ABCDEF')
        self.plaintext = bytes.fromhex('6BC1BEE22E409F96' * 100)
        self.iterations = 1000000

    def test_performance_comparison(self):
        start_time = time.perf_counter()
        for _ in range(self.iterations):
            CryptoWrapper.encrypt_pycryptodome(self.key, self.iv, self.plaintext)
        pycryptodome_time = time.perf_counter() - start_time

        start_time = time.perf_counter()
        for _ in range(self.iterations):
            CryptoWrapper.encrypt_cryptography(self.key, self.iv, self.plaintext)
        cryptography_time = time.perf_counter() - start_time

        print(f"\nPyCryptodome time ({self.iterations} iterations): {pycryptodome_time:.4f}s")
        print(f"Cryptography time ({self.iterations} iterations): {cryptography_time:.4f}s")

        self.assertTrue(pycryptodome_time > 0)
        self.assertTrue(cryptography_time > 0)

if __name__ == '__main__':
    unittest.main()