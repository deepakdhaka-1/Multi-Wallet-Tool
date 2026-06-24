# 🐍 Solana Wallet Generator – `python.py`

Generate multiple Solana wallets with private keys and addresses saved into separate files.

<div align="center">
	<img src="https://img.shields.io/badge/solana-wallet--tool-green?style=for-the-badge&logo=solana" />
	<img src="https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python" />
	<img src="https://img.shields.io/badge/platform-WSL/Linux-lightgrey?style=for-the-badge&logo=ubuntu" />
</div>

---

## 🚀 Features

✅ Generates multiple Solana wallets using `solders`  
✅ Saves:
- `wallet.txt`: Wallet addresses  
- `pvt.csv`: Private key in byte array format  
- `pvt2.csv`: Private key in raw base58 format (no extra symbols)  

✅ Clean format – no quotes, no labels, just data  
✅ Supports Linux, WSL, Ubuntu

---

## 🛠 Requirements

- Python 3.10+
- Install dependencies:

```bash
pip install solders base58
pip install solana
```

## Run Commands - 
```
cd wallet-tools/generate-solana-wallet
```
```
python3 solana.py
```
# Copy Text of file if you are in WSL or Window. Everytime you run `clip.exe` command you it will copy the content on the clipboard.
```
cat wallet.txt | clip.exe   
```
```
cat pvt.csv | clip.exe
```
```
cat pvt2.csv | clip.exe
```