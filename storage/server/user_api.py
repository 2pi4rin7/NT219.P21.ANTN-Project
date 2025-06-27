from flask import Blueprint, request, jsonify
from authorize import check_token

user_api = Blueprint('user_api', __name__)

@user_api.route('/api/user_info', methods=['GET'])
@check_token
def get_user_info(user):
    return jsonify({
        'user_id': user['user_id'],
        'attribute': user['attribute']
    }), 200