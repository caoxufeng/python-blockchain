from flask import Flask, jsonify
from blockchain import Blockchain
import json
app = Flask(__name__)


blockchain = Blockchain()


@app.route("/mine_block")
def mine_block():
    previous_block = blockchain.get_prev_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, hash, "a block")
    response = {'message': 'Congratulations,you just mined a block!',
                'block_content': block}
    return json.dumps(response)


@app.route("/get_chain")
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response)
