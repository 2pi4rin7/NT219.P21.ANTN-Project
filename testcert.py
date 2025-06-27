from Crypto.PublicKey import ECC
from jwt import encode, decode, exceptions
import datetime

# 1. Tạo private & public key trong RAM (ECDSA P-256)
private_key = ECC.generate(curve='P-256')
public_key = private_key.public_key()

private_pem = private_key.export_key(format='PEM')
public_pem = public_key.export_key(format='PEM')

# 2. Tạo JWT
payload = {
    "user_id": 123,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
}

# Ký token với private key (ES256)
token = encode(payload, private_pem, algorithm="ES256")
print("🔐 JWT:", token)

# 3. Xác minh JWT với public key
try:
    decoded = decode(token, public_pem, algorithms=["ES256"])
    print("✅ Verified payload:", decoded)
except exceptions.InvalidTokenError as e:
    print("❌ Invalid token:", str(e))
