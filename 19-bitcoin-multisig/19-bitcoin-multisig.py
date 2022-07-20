from bitcoin import *

# 4 PPKs
private_key1 = random_key()
public_key1 = privtopub(private_key1)

private_key2 = random_key()
public_key2 = privtopub(private_key2)

private_key3 = random_key()
public_key3 = privtopub(private_key3)

private_key4 = random_key()
public_key4 = privtopub(private_key4)

# Multisig public key
multisig = mk_multisig_script(public_key1, public_key2, public_key3, public_key4,4)
print("Multisig: ", multisig)

# Bitcoin address
bitcoin_address = scriptaddr(multisig)
print("Bitcoin address: ",bitcoin_address)