import hashlib

def hash_generator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self, data, hash , prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash


class Blockchain:
    def __init__(self):
        hashlast= hash_generator('gen_last')
        hashstart =hash_generator('gen_hash')


        gensis = Block('gen_data',hashstart, hashlast)
        self.chain =[gensis]

    def add_block(self, data):
            prev_hash = self.chain[-1].hash      ##this the hash of the gensis block
            hash = hash_generator(data + prev_hash)   ## anything you can pass to make it unique afterwards it will form the hexdigits only.
            block = Block(data, hash, prev_hash)     ## block 2 has been created
            self.chain.append(block)


bc=Blockchain()
bc.add_block('1')
bc.add_block('2')
bc.add_block('3')

for block in bc.chain:     ## this code is used to make the directornary of that blockchain.
    print(block.__dict__)

## end of the simple blockcahin projects 