import hashlib

# added visual representation for Blockchain with more interactions

def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()


class Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash


class Blockchain:

    def __init__(self):
        hashLast = hashGenerator('The hash of the last Block')
        hashStart = hashGenerator('The hash of the current Block')
        genesis = Block('The First Block of the Blockchain',
                       hashStart, hashLast)
        self.chain = [genesis]

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data+prev_hash)
        block = Block(data, hash, prev_hash)
        self.chain.append(block)


bc = Blockchain()
ans = ''
while(ans != 'Stop'):
    print('Menu:')
    print('1. Add new data to blockchain\n2. Show Blockchain\n')
    print('Please Enter your Choice to continue otherwise Enter "Stop"')
    ans = input()
    if ans == '1':
        print('Enter data to add in blockchain:')
        str1 = input()
        bc.add_block(str1)
    elif ans == '2':
        f = 0
        for blocks in bc.chain:
            if f == 0:
                print('xxxxxxxxxxxxxxxxxxxx  This is the start of Blockchain  xxxxxxxxxxxxxxxxxxxxxxxx')
                f = 1
            else:
                print('                                         [                                         ')
                print('                                         ]                                         ')
            print('+---------------------------------------------------------------------------------+')
            key1 = list(blocks.__dict__.keys())[0]
            key2 = list(blocks.__dict__.keys())[1]
            key3 = list(blocks.__dict__.keys())[2]
            print('  ',key1, ': ', blocks.__dict__.get(key1))
            print('| ', key2, ': ', blocks.__dict__.get(key2), '      |')
            print('| ', key3, ': ', blocks.__dict__.get(key3), ' |')
            print('|_________________________________________________________________________________|')
            print('                                         [                                         ')
            print('                                         ]                                         ')
