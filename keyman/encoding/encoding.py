import hmac
from pycoin.cmds.ku import get_entropy
import hashlib

def get_chain_secret_pair(netcode='BTC', key='Bitcoin seed', master_secret = None):
    if master_secret is None:
        master_secret = get_entropy()
    I64 = hmac.HMAC(key=key, msg=master_secret,
            digestmod=hashlib.sha512)
    chain_code = I64.digest()[32:]
    secret_exponent = I64.hexdigest()[:64]
    return (chain_code, secret_exponent)
