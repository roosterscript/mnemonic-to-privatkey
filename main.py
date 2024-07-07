from web3 import Web3

# Initialize Web3 instance properly
w3 = Web3()

# Enable unaudited HDWallet features
w3.eth.account.enable_unaudited_hdwallet_features()

# Read mnemonics from file
try:
    with open('mnemonics.txt', 'r') as f:
        mnemonics = [line.strip() for line in f]
except FileNotFoundError:
    print("Error: 'mnemonics.txt' file not found.")
    mnemonics = []

private_keys = []

for mnemonic in mnemonics:
    try:
        account = w3.eth.account.from_mnemonic(mnemonic, account_path="m/44'/60'/0'/0/0")
        private_key = Web3.to_hex(account.key)
        private_keys.append(private_key)
    except ValueError as e:
        print(f"Error processing mnemonic '{mnemonic}': {e}")

# Write private keys to file
try:
    with open('privatekeys.txt', 'w') as f:
        f.writelines(f"{key}\n" for key in private_keys)
except Exception as e:
    print(f"Error writing to 'privatekeys.txt': {e}")

print("Private keys extraction completed.")
