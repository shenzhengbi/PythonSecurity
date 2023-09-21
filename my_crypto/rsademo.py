import rsa
from binascii import b2a_hex

#第一步生成rsa的公钥和私钥
pub,pri = rsa.newkeys(256)
#print(pub,pri)

#使用公钥加密
encrypt = rsa.encrypt('hello蜗牛'.encode(),pub)
# print(encrypt)
# print(b2a_hex(encrypt).decode()) #b2a_hex将二进制字节转换成16进制字节序列

#使用私钥解密
decrypt = rsa.decrypt(encrypt,pri)
print(decrypt.decode())