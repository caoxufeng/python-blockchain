import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Buiding a Blockchain


class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof=1, prev_hash='0', data='gensis block')

    def create_block(self, proof, prev_hash, data):
        block = {'index': len(self.chain) + 1,
                 'data': data,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'prev_hash': prev_hash}

        self.chain.append(block)
        return block

    def get_prev_block(self):
        return self.chain[-1]

    def proof_of_work(self, prev_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof ** 2 - prev_proof ** 2).encode()).hexdigest()

            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    # Part 2 - Mining our Blockchain
    def mining(self, data):
        prev_block = self.get_prev_block()
        new_proof = self.proof_of_work(prev_block['proof'])
        prev_hash = self.hash(prev_block)
        print("prev_hash:", prev_hash)
        self.create_block(new_proof, prev_hash, data)


if __name__ == "__main__":

    ubc = Blockchain()
    ubc.mining("a buy a house.")
    ubc.mining("b buy a car.")

    for i in ubc.chain:
        print(i['data'])
