import struct 
import numpy as np
import os

class blockPrefix(object):
    __slots__ = ('version', 'previousBlock', 'merkleRoot', 'timeStamp', 'bits', 'nonce')

class blockChain(object):
    """Parses a blockchain"""
    _filename = ""

    def loadfile(_self,file):
        _filename = file;

    def blocks(_self):
        if not _filename:
            return
        # TODO find next block in file
        yield block


    def parseBlock(_self, blockChainFile, position=0):
        with open(blockChainFile, "rb") as file:
            file.seek(position, os.SEEK_SET)            
            byte = hex(int.from_bytes(file.read(4), 'little')).upper()           
            if(byte == '0XD9B4BEF9'):
                print("Found Start")
                     

if __name__ == '__main__':
    blockChain().parseBlock('blk00000.dat')



