#测试凯撒密码
def kaiser():
    source  = '蜗牛学院'
    target = ''
    for i in source:
        ascii = ord(i)
        ascii+=1
        ascii = chr(ascii)
        target += ascii

    print(target)

    unravel = ''
    for i in target:
        ascii = ord(i)
        ascii-=1
        unravel+=chr(ascii)

    print(unravel)

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



