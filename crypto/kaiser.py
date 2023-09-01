# 针对中文的凯撒密码

def chinese_kaiser():
    source = '蜗牛学院'

    for c in source:
        ascii = ord(c)
        ascii += 2
        print(chr(ascii), end='')

    print('')

    source = '蜙牝孨除'
    for c in source:
        ascii = ord(c)
        ascii -= 2
        print(chr(ascii), end='')

    print('')


# 栅栏密码

def encrypt(string):
    plaintext = string
    ciphertext1 = ''
    ciphertext2 = ''
    for i in range(len(plaintext)):
        if (i % 2) == 0:
            ciphertext1 += plaintext[i]
        else:
            ciphertext2 += plaintext[i]
    ciphertext = [ciphertext1, ciphertext2]
    return ciphertext


def decrypt(ciphertext1, ciphertext2):  # 解密函数 ，输入密文1，密文2
    plaintext = ''
    for i in range(len(ciphertext1)):
        plaintext += ciphertext1[i]
        if i < len(ciphertext2):
            plaintext += ciphertext2[i]

    return plaintext


# if __name__ == '__main__':
#     chinese_kaiser()
#     ciphertext = encrypt('wearegoodpeople')
#     print(ciphertext)
#     print(decrypt(ciphertext[0], ciphertext[1]))



# 有张三和李四两个人，张三的加密算法是：采用凯撒加密算法，字母右移5位，
# 李四的加密算法是：大小写互换。要求双方在不知道对方加密算法的前提下，
# 双方实现文本的传输，并且确保传输过程始终是加密的。（本题只考虑大小写字母，不考虑数字和其它符号）

# import string
#
# upper_list = string.ascii_uppercase
# lower_list = string.ascii_lowercase
#
# # 可行性分析
# print(upper_list)
#
# # 凯撒加密过程：右移5位
# upper_dest = ''
# for c in upper_list:
#     index = (upper_list.index(c) + 5) % len(upper_list)
#     upper_dest += upper_list[index]
# print(upper_dest)
#
# # 凯撒解密过程：左移5位
# for c in upper_dest:
#     index = upper_dest.index(c) - 5
#     print(upper_dest[index], end='')




import string

upper_list = string.ascii_uppercase
lower_list = string.ascii_lowercase

# source = HelloWoniu

# 对大小写利用凯撒算法右移5位
def encrypt_zhang(source):
    dest = ''
    for c in source:
        # 如果是大写的情况
        if c in upper_list:
            index = (upper_list.index(c) + 5) % 26
            dest += upper_list[index]
        elif c in lower_list:
            index = (lower_list.index(c) + 5) % 26
            dest += lower_list[index]
    return dest

# 对凯撒加密后的字符串进行左移5位实现解密
def decrypt_zhang(source):
    dest = ''
    for c in source:
        if c in upper_list:
            index = (upper_list.index(c) - 5)
            dest += upper_list[index]
        elif c in lower_list:
            index = (lower_list.index(c) - 5)
            dest += lower_list[index]
    return dest

# 李四的算法是大小写互换，所以加密解密算法是一样的
def convert_li(source):
    dest = ''
    for c in source:
        if ord(c) >= 65 and ord(c) <= 90:
            dest += chr(ord(c) + 32)
        elif ord(c) >= 97 and ord(c) <= 122:
            dest += chr(ord(c) - 32)
    return dest


if __name__ == '__main__':
    # 此加密解密过程可以称之为非对称加密，但是目前我们主流的非对称加密主要是指公钥私钥对
    source = 'HelloWoniu'
    print(source)
    result_1 = encrypt_zhang(source)
    print(result_1)
    result_2 = convert_li(result_1)
    print(result_2)
    result_3 = decrypt_zhang(result_2)
    print(result_3)
    result_4 = convert_li(result_3)
    print(result_4)