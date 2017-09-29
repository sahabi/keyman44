import hmac
from pycoin.cmds.ku import get_enropy

def get_master_secret(netcode='BTC', key='Bitcoin seed', master_secret = None):
    if master_secret is None:
        master_secret = get_entropy()
    I64 = hmac.HMAC(key=key, master_secret = master_secret,
            digestmod=hashlib.sha512).digest()
    chain_code = I64[32:]
    secret_exponent = I64[:32]
    return (chain_code, secret_exponent)
