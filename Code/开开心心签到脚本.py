a='617363725d71154a454b437952167961736372794f5279175579411616425b'
alice=bytes.fromhex(a)
result=bytes(b^0x26 for b in alice)
result=result.decode('utf-8')
print(result) 