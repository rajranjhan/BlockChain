import hashlib

class BitcoinClient(object):
    """
    bitcoin client
    """

    def proofOfWork(_self, data, target):
        nonce = 0;

        while True:
            hexDig = hashlib.sha256((data + str(nonce)).encode()).hexdigest()                        
            if hexDig.startswith(target):
                return hexDig, nonce                
            nonce += 1
             
if __name__ == '__main__': 
    client = BitcoinClient()
    hashedValue, nonce = client.proofOfWork('This is a string', '0000')
    print(hashedValue)
    print(nonce)
