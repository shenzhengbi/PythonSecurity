from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
#补位，aes每组必须是128位（16个字节，一个字节8位，不够的用空格补位）

source = 'hello-蜗牛'
if len(source.encode('utf-8')) % 16:
    add = 16-(len(source.encode('utf-8'))%16)
else:
    add =0

source = source + ('\0'*add)
#print(source)

# 定义密钥和偏移量，必须是16个字节、24字节或32字节
# key = 'todayiswonderful-1234567'.encode()
key = 'todayiswonderful-FEDCBA987654321'.encode()
mode = AES.MODE_CBC  #aes中cbc才需要设置偏移量
iv = b'1234567890ABCDEF'
cryptos = AES.new(key, mode, iv)

cipher = cryptos.encrypt(source.encode())
print(cipher)
print(b2a_hex(cipher).decode())

#解密
key = 'todayiswonderful-FEDCBA987654321'.encode()
mode = AES.MODE_CBC
iv = b'1234567890ABCDEF'
cryptos = AES.new(key, mode, iv)

source = '9b65cecd512fb46558b4db090d60ee81'
dest = cryptos.decrypt(a2b_hex(source))
print(dest.decode().rstrip('\0'))