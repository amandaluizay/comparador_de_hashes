import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

# le o arquivo e transforma ele em hash usando algaritimo ripemd
hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

# compara se os dois são iguais, método digest resume o hash
if hash1.digest() != hash2.digest():
    print(f'O arquivo : {arquivo1} é diferente do {arquivo2}')
else:
    print(f'O arquivo {arquivo1} é igual ao {arquivo2}')
