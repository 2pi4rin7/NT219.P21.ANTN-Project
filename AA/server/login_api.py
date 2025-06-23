from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for
from processing import authenticate_user
from pymongo import MongoClient
import hashlib
login_api = Blueprint('login_api', __name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['healthcare']
users_collection = db['users']

# Route to render login page
@login_api.route('/', methods=['GET'])
def login_page():
    return render_template('login.html')


# Handle login form submission
@login_api.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return "Missing username or password", 400

    user = authenticate_user(username, password)
    if user:
        user['_id'] = str(user['_id'])  # Convert ObjectId to str
        session['user'] = user
        if ('admin' in user.get('attribute', [])):
            return redirect(url_for('login_api.register_page'))
        else:
            return jsonify(user), 200
    else:
        return "Invalid username or password", 401


# Route to render register page
@login_api.route("/register", methods=["GET"])
def register_page():
    if 'user' not in session:
        return redirect(url_for('login_api.login_page'))
    if 'admin' not in session['user'].get('attribute', []):
        return "Forbidden", 403
    return render_template('register.html')


# Handle register form submission
@login_api.route("/register", methods=["POST"])
def register():
    if 'user' not in session:
        return redirect(url_for('login_api.login_page'))
    if 'admin' not in session['user'].get('attribute', []):
        return "Forbidden", 403

    username = request.form.get('username')
    password = request.form.get('password')
    attribute = request.form.get('attribute')
    ATR = attribute.replace(" ", "").split(",") if attribute else []

    usercount = users_collection.count_documents({})

    new_user = {
        "username": username,
        "password": hashlib.sha256(password.encode()).hexdigest(),
        "ID": str(usercount + 1),
        "attribute": ATR
    }
    users_collection.insert_one(new_user)
    return render_template('register.html', message="User registered successfully")
