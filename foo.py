import hashlib

digits = "0123456789abcdefjhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"
a = hashlib.md5(b"ss").hexdigest()
print(a)

print(int(a, 16))
str = bin(int(a, 16))[2:]
for i in range(6):
    s6 = str[i*6:i*6 + 6]
    print(digits[int(s6,2)])