# EVM Wallet Generator

This folder contains the current EVM wallet generator implementation.

## What it does

- Generates BIP39 mnemonic phrases.
- Derives an EVM account from each mnemonic.
- Writes the mnemonic, private key, and wallet address to `evm_wallets.csv`.

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python bot.py
```

## Output

The generator creates a CSV file in the working directory where you run the script.