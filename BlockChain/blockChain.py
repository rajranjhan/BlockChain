import struct 
import numpy as np
import os
class BlockPrefix(object): #Must be new-style class!
    #slots save memory in 
    __slots__ = ['version', 'previousBlock', 'merkleRoot', 'timeStamp', 'bits', 'nonce']

class BlockChain(object):
    """Parses a blockchain"""
    #Constants
    BLOCK_LEN_BYTES = 4
    
    #properties
    _filename = ""
    _currentFilePos = 0


    def loadfile(_self,file):
        _filename = file;

    def blocks(_self):
        if not _filename:
            return
        # TODO find next block in file
        while True:
            (_currentFilePos, block) = getBlock(_filename, _currentFilePos)
            if(_currentFilePos != -1) :
                yield block
            else:
                break

    def getBlock(_self, blockChainFile, position=0):
        with open(blockChainFile, "rb") as file:
            file.seek(position, os.SEEK_SET)            
            byte = hex(int.from_bytes(file.read(4), 'little')).upper()    
            if(byte == '0XD9B4BEF9'):
                #read number of bytes in the block.  
                # unpack returns a tuple of 
                # '<' = little endian, 'i' = integer
                blockLength, = struct.unpack('<i', file.read(_self.BLOCK_LEN_BYTES))
                blockPrefix = BlockPrefix()
                block = file.read(blockLength)
                return block

     def parseBlock(_self, block):                      
                blockPrefix = BlockPrefix()
                blockPrefix.version, = struct.unpack('<i', block(_self.BLOCK_LEN_BYTES))
                return block
                             

if __name__ == '__main__':
    blockChain = BlockChain('blk00000.dat')
    for b in blockChain.blocks:
        blockPrefix = blockchain.parseBlock(b)


