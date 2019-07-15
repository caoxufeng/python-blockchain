from flask import Flask
from blockchain import Blockchain
import json
app = Flask(__name__)


blockchain = Blockchain()


# @app.route("/a", methods=['GET', 'POST'])
# def home():
#     return "hi"

@app.route('/')
def hello_world():
    return 'Hello, World!'


# @app.route("/mine_block", methods=['GET', 'POST'])
# def mine_block():
#     previous_block = blockchain.get_prev_block()
#     previous_proof = previous_block['proof']
#     proof = blockchain.proof_of_work(prev_proof)
#     hash = blockchain.hash(previous_block)
#     block = blockchain.create_block(proof, prev_hash)
#     response = {'message': 'Congratulations,you just mined a block!',
#                 'block_content': block}
#     return json.dumps(response)
