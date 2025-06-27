# trusted_authority/server/auth_api.py
from flask import Blueprint, request, jsonify, session
import jwt
import datetime
import os
from Crypto.PublicKey import ECC


auth_api = Blueprint('auth_api', __name__)


with open('./opt/jwtkey_priv.pem', 'r') as f:
    SECRET_KEY = ECC.import_key(f.read())
SECRET_KEY = SECRET_KEY.export_key(format='PEM')
@auth_api.route('/token', methods=['POST'])
def get_token():
    data = request.json
    if not data or '_id' not in data:
        return "Invalid request", 400
    
    token = jwt.encode({
        'user_id': data['ID'],
        'attribute': str(data['attribute']),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, SECRET_KEY, algorithm='ES256')
    
    return token, 200