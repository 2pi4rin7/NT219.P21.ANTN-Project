from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from charm.core.engine.util import objectToBytes, bytesToObject

# Your ABE class
class ABE:
    def __init__(self):
        self.group = PairingGroup('SS512')
        self.cpabe = HybridABEnc(CPabe_BSW07(self.group), self.group)
        self.sign = b'DEADBEEF'

    def encrypt(self, pk_bytes, msg, policy):
        pk = bytesToObject(pk_bytes, self.group)
        ct = self.cpabe.encrypt(pk, msg, policy)
        return ct
    
    def decrypt(self, pk_bytes, sk_bytes, ct):
        pk = bytesToObject(pk_bytes, self.group)
        sk = bytesToObject(sk_bytes, self.group)
        return self.cpabe.decrypt(pk, sk, ct)


# --------- Setup Phase ---------
group = PairingGroup('SS512')
cpabe = HybridABEnc(CPabe_BSW07(group), group)

# Generate keys
(pk, mk) = cpabe.setup()
attributes = ['doctor', 'cardiologist']
sk = cpabe.keygen(pk, mk, attributes)

# Serialize pk and sk
pk_bytes = objectToBytes(pk, group)
sk_bytes = objectToBytes(sk, group)

# --------- Use ABE class ---------
abe = ABE()

# Encrypt
policy = 'doctor OR cardiologist'
message = b"Confidential patient data"
ciphertext = abe.encrypt(pk_bytes, message, policy)

# Decrypt
try:
    decrypted = abe.decrypt(pk_bytes, sk_bytes, ciphertext)
    print("Original:", message)
    print("Decrypted:", decrypted)
    print("Match:", message == decrypted)
except Exception as e:
    print("Decryption failed:", e)
