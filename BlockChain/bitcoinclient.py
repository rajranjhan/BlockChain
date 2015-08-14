import hashlib

class BitcoinClient(object):
    """
    bitcoin client
    """

    def proofOfWork(_self, data, target):
        nonce = 0;

        while True:
            hash_object = hashlib.sha256(data + nonce).hexdigest()            
            print(hex_dig)                 
            nonce += 1
            if nonce == 5:
                break


if __name__ == '__main__': 
    client = BitcoinClient()
    client.proofOfWork('This is a string', '0000')
