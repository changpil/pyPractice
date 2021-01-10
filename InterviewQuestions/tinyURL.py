# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
# Design the encode and decode methods for the TinyURL service.
# There is no restriction on how your encode/decode algorithm should work.
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

import random
import os
class Codec:
    lurl_map = {}
    surl_map = {}
    prefix = "http://tinyurl.com/"
    q = []
    digit = 4
    seed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    threshold = 10
    def encode(self, longUrl: str) -> str:
        if longUrl in Codec.lurl_map:
            return Codec.lurl_map[longUrl]

        if len(Codec.q) != 0:
            return Codec.q.pop()

        while True:
            candidate = ""

            for _ in range(Codec.threshold):
                for _ in range(Codec.digit):
                    candidate += random.choice(Codec.seed)

                if candidate not in Codec.lurl_map:
                    candidate = Codec.prefix + candidate
                    Codec.lurl_map[longUrl] = candidate
                    Codec.surl_map[candidate] = longUrl
                    return Codec.lurl_map[longUrl]
            Codec.digit += 1
        return -1

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl not in Codec.surl_map:
            return -1
        return Codec.surl_map[shortUrl]
# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.decode(codec.encode("https://pynative.com/python-random-choice/")))
print(codec.encode("https://pynative.com/python-random-choice/"))
