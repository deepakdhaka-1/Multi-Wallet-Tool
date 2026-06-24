import secrets
from mnemonic import Mnemonic
from eth_account import Account


def generate_mnemonic():
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.generate(strength=128)
    return mnemonic_phrase


def mnemonic_to_keypair(mnemonic_phrase):
    Account.enable_unaudited_hdwallet_features()
    account = Account.from_mnemonic(mnemonic_phrase)
    private_key = account.key.hex()
    wallet_address = account.address
    return private_key, wallet_address


def mass_generate_wallets(n):
    wallet_data = []
    for i in range(n):
        mnemonic = generate_mnemonic()
        private_key, wallet_address = mnemonic_to_keypair(mnemonic)
        wallet_data.append((mnemonic, private_key, wallet_address))
        print(f"[{i+1}] Address: {wallet_address}")
    return wallet_data


def save_to_csv(wallet_data, filename="evm_wallets.csv"):
    with open(filename, 'w') as f:
        f.write("Mnemonic,PrivateKey,WalletAddress\n")
        for mnemonic, private_key, wallet_address in wallet_data:
            f.write(f'"{mnemonic}","{private_key}","{wallet_address}"\n')


def main():
    count = int(input("Enter the number of EVM wallets to generate: "))
    wallets = mass_generate_wallets(count)
    save_to_csv(wallets)
    print(f"\n✅ {count} wallets saved to 'evm_wallets.csv' with mnemonic, key, and address.")


if __name__ == "__main__":
    main()