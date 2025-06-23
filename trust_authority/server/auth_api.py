# trusted_authority/server/auth_api.py
from flask import Blueprint, request, jsonify, session
import jwt
import datetime
import os

auth_api = Blueprint('auth_api', __name__)

# Tạo secret key ngẫu nhiên
SECRET_KEY = "1508a86b981913fb2f065068aa5ee3203a8366dce9505459e9683aa1171c10f7"

@auth_api.route('/token', methods=['POST'])
def get_token():
    data = request.json
    if not data or '_id' not in data:
        return "Invalid request", 400
    
    # Tạo token với thời hạn 24 giờ
    token = jwt.encode({
        'user_id': data['ID'],
        'attribute': str(data['attribute']),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, SECRET_KEY, algorithm='HS256')
    
    return token, 200