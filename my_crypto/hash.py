#可逆加密（对称加密，非对称加密，这些已知密文和秘钥可以得到明文）
#非可逆加密（根据密文无法解密，如md5，sha，这些主要用于数字签名密码等）

import hashlib
def hash():
    source = "你好 蜗牛"
    print(hashlib.md5(source.encode()).hexdigest())

    with open('./test.jpg',mode='rb') as file:
       data = file.read()

    print(hashlib.md5(data).hexdigest())

#SHA也是摘要算法，与MD5用法一致，差别在于SHA可以有不同的位数设定，强度可以更高


#作业题，非对称加密，张三和李四通信，张三的加密算法：凯撒算法，右移5位，李四加密算法大小写互换，传输过程中都是加密的密文。
#思路，张三先加密，将密文给李四，李四再加密，将张三李四共同加密的密文再发送给张三，张三解密，将只有李四加密的密文给李四，李四再解密。

import kaiser
#大小写互换，数字移位
def A_a(source):
    target = ''
    for i in source:
        if ord(i) in range(65,91):
            temp = chr(ord(i)+32)
        elif ord(i) in range(97,123):
            temp = chr(ord(i)-32)
        target+=temp

    return target

if __name__ == "__main__":
    source = "azazadfls"
    flag = 5

    #张三加密
    zs_en = kaiser.encode_kaiser(source,flag)
    print(zs_en)
    #李四加密
    lszs_en = A_a(zs_en)
    print(lszs_en)
    #张三解密
    ls_en = kaiser.decode_kaiser(lszs_en,flag)
    print(ls_en)
    #李四解密
    en = A_a(ls_en)
    print(en)