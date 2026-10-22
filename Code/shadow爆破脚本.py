import hashlib
alice=('d0b53d421c50a45a5ef735b4725c2c9a123862779c50e95d284c476bdf469b29')
sora=('cd46936c5c396f66b2971b12d427563a3b0d9a671a8ee0e9eb7e809571d3ddb7')
amy=('0f9fd014')
elma=('35712258')
for i in range(1000000):  #穷举六位整数
  a=f"{i:06d}"              #格式化输入不足六位的前面补零
  a=bytes(a.encode('utf-8'))#转为字节串
  akana_bytes=hashlib.sha256(amy.encode()+a).hexdigest()#做算法转为16进制字符串
  nbn_bytes=hashlib.sha256(elma.encode()+a).hexdigest()
  if akana_bytes==alice and nbn_bytes==sora:     
    print(a.decode('utf-8'))#重新变回字符串
    break
else:
  print("bad")