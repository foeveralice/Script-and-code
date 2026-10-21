amy, alice=input("请输入你的数据喵: ").split()#输入两个数据
amy=bytes.fromhex(amy)#从16进制字符串中转换
code2=[ord(c) for c in alice]#将文字转为ascii码
code1=amy
code2.reverse()#取反向
def elma(code1,code2):
    result=bytes(b^code2[i%len(code2)] for i, b in enumerate(code1))#做循环异或
    result=result.decode('ascii')#从字节数转为ascii码对应字符
    print(result)
elma(code1,code2)    
