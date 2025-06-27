from flask import Flask, session
import os
from login_api import login_api
from auth_api import auth_api
from gen_keys_api import gen_keys_api
from processing import create_sample_users

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'

app.register_blueprint(login_api)
app.register_blueprint(auth_api)
app.register_blueprint(gen_keys_api)

create_sample_users()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)