elma={'南':'1','北':'0','绿':'3','豆':'2'}#用元组对应数字
alice='南北南绿 南南南南 南北南南 南南南北 南绿豆绿 南绿南绿 北绿北北 南南绿绿 南绿南绿 南北绿绿 南南绿绿 南南南绿 南豆绿绿'
amy=alice.split()#用split转成列表
end=''#为后面连接准备
for i in amy:
  akana="".join(elma[k] for k in i)#将其转为四进制数
  aka=int(akana,4)
  aka=chr(aka)
  end=end+aka
print(end)  
  
