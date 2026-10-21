
alice=('58 28 47 d2 84 7d 70 07 d1 12 2f 52 aa 47 58 a6 3d 3e 24 33 32 0b 1e 13 07 19 20 0e 18 0a 08 1f 17 3b 08 0d 1c')
alice=bytes.fromhex(alice)#转字节串
alice=bytes(b^0xA7 for b in alice)#逐字节异或
for i in range(11):            #行数，一共9行
  for k in range(11):           #列数，一共10列
    amy=k+11*i
    elma=(alice[(amy>>3)%len(alice)]>>(amy&7))&1
    if elma==1:
      print('#',end='')#输出#号作为墙空格分隔
    else:
      print('.',end='')#.号为路径
  print()#换下一行      
    

      
