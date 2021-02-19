# Want to dynamically configure algorithm

class File:
    def __init__(self,):
        self.strategy = None

    def compress(self):
        self.strategy.compress()

import abc
class CompressionStrategy(abc.ABC):
    @abc.abstractmethod
    def compress(cls):
        pass

class ZipCompression(CompressionStrategy):
    def compress(cls):
        print("zip Compression")

class RarCompression(CompressionStrategy):
    def compress(cls):
        print("rar Compression")

f = File()
f.strategy = ZipCompression()
f.compress()

f.strategy = RarCompression()
f.compress()