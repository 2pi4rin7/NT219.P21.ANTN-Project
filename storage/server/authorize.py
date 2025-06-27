from flask import request, jsonify
from functools import wraps
import jwt
import os
from ast import literal_eval
from Crypto.PublicKey import ECC

with open('./opt/jwtkey_pub.pem', 'rb') as f:
    PUBLIC_KEY = ECC.import_key(f.read())
PUBLIC_KEY = PUBLIC_KEY.export_key(format='PEM')

def check_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        
        if not token:
            return jsonify({'error': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, PUBLIC_KEY, algorithms=['ES256'])
            user = {
                'user_id': data['user_id'],
                'attribute': data['attribute']
            }
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token!'}), 401
        
        return f(user, *args, **kwargs)
    
    return decorated