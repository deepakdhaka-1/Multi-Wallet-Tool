import csv
from bip_utils import Bip39SeedGenerator, Bip39MnemonicGenerator, Bip39WordsNum, Bip44, Bip44Coins, Bip44Changes
from eth_account import Account

# Enable legacy key derivation for eth_account
Account.enable_unaudited_hdwallet_features()


def generate_mnemonic():
    return Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)


def derive_wallets(mnemonic: str, count: int):
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    bip44_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)

    wallets = []
    for i in range(count):
        bip44_wallet = bip44_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(i)
        private_key = bip44_wallet.PrivateKey().Raw().ToHex()
        account = Account.from_key(private_key)
        wallets.append({
            "private_key": private_key,
            "address": account.address
        })
    return wallets


def save_wallets_to_csv(wallets, filename="evm_wallets.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["private_key", "address"])
        for wallet in wallets:
            writer.writerow([wallet["private_key"], wallet["address"]])


def main():
    count = int(input("🔢 Enter number of sub-wallets to generate: "))
    mnemonic = generate_mnemonic()

    print("\n🌱 Your 24-word Seed Phrase (SAVE THIS SAFELY):")
    print(mnemonic)

    wallets = derive_wallets(mnemonic, count)
    save_wallets_to_csv(wallets)

    print(f"\n✅ {count} wallets generated.")
    print("📁 Wallets saved to: evm_wallets.csv")


if __name__ == "__main__":
    main()