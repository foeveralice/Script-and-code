amy="7821352D093A1B6C39011A3B2844200C2B024A335231706F5E002D1801174C00021C130E13"
alice='H0w_t0_3ncrypt?'
amy=bytes.fromhex(amy)#从16进制字符串中转换
code2=[ord(c) for c in alice]#将文字转为ascii码
code1=amy
code2.reverse()#取反向
def elma(code1,code2):
    result=bytes(b^code2[i%len(code2)] for i, b in enumerate(code1))#做循环异或
    result=result.decode('ascii')#从字节数转为ascii码对应字符
    print(result)
elma(code1,code2)    
