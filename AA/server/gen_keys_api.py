from flask import Blueprint, request, jsonify
from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.core.engine.util import objectToBytes
from Crypto.PublicKey import ECC
import json

gen_keys_api = Blueprint('gen_keys_api', __name__)

group = PairingGroup('SS512')
cpabe = CPabe_BSW07(group)
(master_public_key, master_key) = cpabe.setup()

@gen_keys_api.route('/get_keys', methods=['POST'])
def get_keys():
    data = request.json
    if not data or 'attribute' not in data:
        return "Invalid request", 400
    
    try:
        attributes = eval(data['attribute'])
        
        dk_key = cpabe.keygen(master_public_key, master_key, attributes)
        
        pk_bytes = objectToBytes(master_public_key, group)
        dk_bytes = objectToBytes(dk_key, group)
        
        return jsonify({
            'pk_key': pk_bytes.decode(),
            'dk_key': dk_bytes.decode()
        }), 200
    except Exception as e:
        return str(e), 500