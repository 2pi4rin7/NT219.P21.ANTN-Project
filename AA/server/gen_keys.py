from flask import Blueprint, request, jsonify
from Crypto.PublicKey import ECC
import os

os.makedirs('./opt', exist_ok=True)

private_key = ECC.generate(curve='P-256')
public_key = private_key.public_key()

private_pem = private_key.export_key(format='PEM')
public_pem = public_key.export_key(format='PEM')


with open('./opt/jwtkey_priv.pem', 'w') as f:
    f.write(private_pem)

with open('./opt/jwtkey_pub.pem', 'w') as f:
    f.write(public_pem)
