# 🔐 EVM Sub-Wallet Generator CLI

A powerful command-line tool to generate multiple EVM sub-wallets derived from a single secure BIP39 mnemonic seed phrase. Perfect for developers, testers, and crypto automation tasks like airdrops or faucet farming.

---

## 🚀 Features

- 🌱 **One seed, many wallets** – Generates multiple EVM sub-wallets from a single 24-word mnemonic using BIP32 HD derivation
- 🔑 Each sub-wallet includes:
	- Private key
	- Wallet address
- 📥 Outputs all data to a clean, comma-separated CSV file: `evm_wallets.csv`
- ⚙️ Uses standard EVM derivation path:  
	`m/44'/60'/0'/0/i` where `i` = sub-wallet index
- 🔐 Mnemonic is displayed in the terminal (not stored in file)
- 💨 Fast – generates 100s of wallets in seconds
- 💡 Easy to extend for CSV/JSON/QR export or custom logic

---

## 🛠 Installation

```bash
cd evm-sub-wallet-generator
pip install -r requirements.txt
```
## Main command
```bash
python3 bot.py
# or
python bot.py
```
# To Copy content of wallet `evm_wallets.csv` file.
```bash
cat evm_wallets.csv | clip.exe
```
-This command will copy the content of evm wallets on your clipboard, paste it in any excel or safe location.
-Content is seperated by commas ( , )