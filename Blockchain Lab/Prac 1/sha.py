import hashlib
import datetime
  
chain = []

class Block:
    def _init_(self,index,nonce,previous_hash,message):
        self.index = index
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.message = message
        self.timestamp = str(datetime.datetime.now())

def printChain():
    for block in chain:
        print("----------")
        print("Index: ",block.index)
        print("Nonce: ",block.nonce)
        print("Previous Hash: ",block.previous_hash)
        print("Current Hash: ",getHash(block))
        print("Message: ",block.message)
        print("Timestamp: ",block.timestamp)

def getHash(block):
    return hashlib.sha256(str(block).encode()).hexdigest()

def getPreviousHash():
    if len(chain)==0:
        previous_hash = 0
    else:
        previous_hash = getHash(chain[-1])
    return previous_hash

def addNewBlock(message):
    nonce = 0
    if len(chain)==0:
        previousNonce = 0
    else:
        previousNonce = chain[-1].nonce
    
    
    while True:
        nonce = nonce + 1
        hashValidator = hashlib.sha256(str(previousNonce*2 - nonce*2).encode()).hexdigest()
        if hashValidator[:4] == '0000':
            newBlock = Block(len(chain)+1,nonce,getPreviousHash(),message)
            chain.append(newBlock)
            return

msg = input("Enter you data to be added in the blockchain: ")
while msg != "-1":
    addNewBlock(msg)
    printChain()
    print("\nFor exit type -1")
    msg = input("\nEnter you data to be added in the blockchain: ")
