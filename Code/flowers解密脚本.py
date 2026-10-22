a=bytes.fromhex("1f1737db9ce063944a4abae12c45da7293d864656c734eb46b701c23c3")
b=bytes.fromhex("0c031c001208050f01170a06140410021b090d1507110e180b13161a19")
c=bytes.fromhex("2cb1fa402ed1df3b371f435648addae77b4a333e301298d49c00000000")


alice=[None]*29
result=bytes(a[i] ^ c[(7*i+3)%0x19] for i in range(0,29))#根据算法得到
for amy,elma in zip(result,b):#用zip，可以一次遍历两个迭代对象
   alice[elma]=amy            #根据伪代码算法
alice=bytes(alice)
alice=alice.decode('ascii')   
print(alice)


