#测试凯撒密码
def encode_kaiser(source,flag):
#加密右移
    target = ''
    for i in source:
        ascii = ord(i)
        ascii+=flag
        if (ascii not in range(65,91)) and (ascii not in range(97,123)):
            if ascii>122:
                ascii = 97 + (ascii - 123)
            else:
                ascii = 65 + (ascii - 91)
        ascii = chr(ascii)
        target += ascii

    return target

def decode_kaiser(source,flag):
    unravel = ''
    for i in source:
        ascii = ord(i)
        ascii-=flag
        if (ascii not in range(65,91)) and (ascii not in range(97,123)):
            if ascii<65:
                ascii = 91 - (65 -ascii)
            else:
                ascii = 123 - (97 - ascii)
        unravel+=chr(ascii)

    return unravel

#栅栏密码加密和解密过程
def encrypt(string):
    text1 = ''
    text2 = ''
    for i in range(len(string)):
        if i%2==0:
            text1+=string[i]
        else:
            text2+=string[i]

    return [text1,text2]

def decrypt(list):
    text1 = list[0]
    text2 = list[1]
    string= ''
    for i in range(len(text1)):
        string+=text1[i]
        if i < len(text2):
            string+=text2[i]

    return string

if __name__ == '__main__':
    list = encrypt('abcdefghijklmnopqistuvwxyza')
    print(list)
    string = decrypt(list)
    print(string)



