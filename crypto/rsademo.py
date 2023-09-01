import rsa
from binascii import b2a_hex, a2b_hex

# 第一步：生成RSA公钥和私钥
# pub, priv = rsa.newkeys(256)
pub, priv = rsa.newkeys(2048)
print(pub, priv)

# 第二步：公钥加密
encrypt = rsa.encrypt('Hello-蜗牛'.encode(), pub)
print(encrypt)
encstr = b2a_hex(encrypt).decode()
print(encstr)

# 第三步：私钥解密
# decrypt = rsa.decrypt(encrypt, priv)
decrypt = rsa.decrypt(a2b_hex(encstr), priv)
print(decrypt.decode())