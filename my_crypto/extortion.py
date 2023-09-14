import base64

#针对某文件进行base64转码加密保存
import os


def encrypt(filepath):
    with open(filepath,mode='rb') as file:
        data = file.read()

    source = base64.b64encode(data).decode()
    #print(source)
    dest = ''
    for c in source:
        dest += chr(ord(c)+5)

    #将加密字符串保存到文件中
    with open(filepath+'.enc',mode='w') as file:
        file.write(dest)
    os.remove(filepath)
def decrypt(filepath):
    with open(filepath,mode='r') as file:
        data = file.read()

    dest = ''
    for c in data:
        dest += chr(ord(c) - 5)
    #dest = dest.encode()

    source = base64.b64decode(dest)

    newfile = filepath.replace('.enc','')
    with open(newfile,mode='wb') as file:
        file.write(source)
    os.remove(filepath)

if __name__ == "__main__":
    encrypt('./test.jpg')
    decrypt('./test.jpg.enc')