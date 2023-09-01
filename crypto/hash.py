# 可逆加密（已知密文，可以解开明文）：对称加密（密钥是同一个），非对称加密（公钥加密，私钥解密，HTTPS）
# 不可逆加密（根据密文无法解密）：哈希算法，散列算法，摘要算法，通常用于数字指纹，MD5，SHA

# 摘要算法的应用场景：
# 1、数字签名
# 2、密码
import hashlib

source = "Hello你好欢迎"
print(hashlib.md5(source.encode()).hexdigest())

source = "Hello 你好欢迎"
print(hashlib.md5(source.encode()).hexdigest())

source = '''
该算法被设计用来把任意序列的8位字节描述为一种不易被人直接识别的形式，达到一眼望去完全看不出内容。
此算法的复杂程度要小，效率高。如果是基于以上两点，那么我们使用最简单的单字母代替法等即可，
实际上Base64要稍微复杂些，这是因为在Email的传送过程中，由于历史原因，Email只被允许传送ASCII字符
'''
print(hashlib.md5(source.encode()).hexdigest())

with open('./test.jpg', mode='rb') as file:
    data = file.read()

print(hashlib.md5(data).hexdigest())

# SHA也是摘要算法，与MD5的用法完全一致，差别在于SHA可以有不同的位数设定，强度可以更高
print(hashlib.sha256(source.encode()).hexdigest())

