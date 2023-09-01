from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

# 加密过程
source = 'Hello-蜗牛难道不是吗也许'

# 如果source分组后剩余长度不足16位的倍数就用空格补足为16位
if len(source.encode('utf-8')) % 16:
    add = 16 - (len(source.encode('utf-8')) % 16)
else:
    add = 0
source = source + ('\0' * add)
print(source)

# 定义密钥和偏移量，必须是16个字节、24字节或32字节
# key = 'todayiswonderful-1234567'.encode()
key = 'todayiswonderful-FEDCBA987654321'.encode()
mode = AES.MODE_CBC
iv = b'1234567890ABCDEF'
cryptos = AES.new(key, mode, iv)

cipher = cryptos.encrypt(source.encode())
print(cipher)
print(b2a_hex(cipher).decode())



# 解密
source = 'f0c0ba97df33f91fdbfacd99c38838f347831e7e3a1f893f6752cdd080fc1c83cb300c0b7e117d587d7e5a69dbb70aee'

key = 'todayiswonderful-FEDCBA987654321'.encode()
mode = AES.MODE_CBC
iv = b'1234567890ABCDEF'
cryptos = AES.new(key, mode, iv)

dest = cryptos.decrypt(a2b_hex(source))
print(dest.decode().rstrip('\0'))