import hashlib
from struct import pack, unpack, unpack_from
from binascii import unhexlify
from bitcoin.rpc import RawProxy
import datetime, calendar
import sys

p = RawProxy()
blockheight = int(sys.argv[1])

blockhash = p.getblockhash(blockheight)
block = p.getblock(blockhash)

version = pack('<I', block['version']).encode('hex_codec')    
prevHash = block['previousblockhash'].decode('hex')
prevHash = prevHash[::-1].encode('hex_codec')
merkleRoot = block['merkleroot'].decode('hex')
merkleRoot = merkleRoot[::-1].encode('hex_codec')
timestamp = pack('<I', block['time']).encode('hex_codec')
bits = pack('<I', int(block['bits'], 16)).encode('hex_codec') 
nonce = pack('<I', block['nonce']).encode('hex_codec') 

headerHex = (version + prevHash + merkleRoot + timestamp + bits + nonce)
headerByte = headerHex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(headerByte).digest()).digest()
hash = hash[::-1].encode('hex_codec')

if hash == block['hash']:
    print("[V] Bloko hash'as yra teisingas!")
else:
    print("[X] Bloko hash'as yra neteisingas!")