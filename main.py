from web3 import Web3

w3 = Web3()
w3.eth.account.enable_unaudited_hdwallet_features()

with open('mnemonics.txt', 'r') as f:
    mnemonics = [line.strip() for line in f]

private_keys = []
for mnemonic in mnemonics:
    account = w3.eth.account.from_mnemonic(mnemonic, account_path="m/44'/60'/0'/0/0")
    private_key = Web3.to_hex(account.key)
    private_keys.append(private_key)


with open('privatekeys.txt', 'w') as f:
    f.writelines(f"{item}\n" for item in private_keys)
