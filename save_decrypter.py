import base64,zlib,os,struct

# decrypter code is stolen from https://pastebin.com/JakxXUVG by Absolute Gamer
# encrypter code is also stolen from https://github.com/WEGFan/Geometry-Dash-Savefile-Editor/ by WEGFan

# i'm not smart enough for this shi im sorry :sob:

saves = ['CCLocalLevels2.dat']
 
def Xor(path,key):
    fr = open(path,'rb')
    data = fr.read()
    fr.close()
    
    res = []
    for i in data:
        res.append(i^key)
    return bytearray(res).decode()
 
def Decrypt(data):
    return zlib.decompress(base64.b64decode(data.replace('-','+').replace('_','/').encode())[10:],-zlib.MAX_WBITS)


fPath = "./backups/Dummy/"
res = Xor(fPath+saves[0],11)
fin = Decrypt(res)

fw = open('./decrypted/' + saves[0] +'.xml','wb')
fw.write(fin)
fw.close()