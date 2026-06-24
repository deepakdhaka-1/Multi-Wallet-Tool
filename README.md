# Multi Wallet Tools

This is the main information source for the consolidated wallet workspace. Each wallet project stays in its own folder under `wallet-tools/`, while this README explains the full layout, usage, and housekeeping rules.

## ✨ Quick Start

1. Open the folder you want to run.
2. Install that tool's requirements.
3. Run the matching entrypoint.

If you are not sure where something lives, start with the map below.

## Workspace layout

```text
wallet-tools/
  evm-wallet-generator/
  generate-solana-wallet/
  evm-sub-wallet-generator/
  kaspa-wallet-generate/
```

## What lives where

- [wallet-tools/evm-wallet-generator](wallet-tools/evm-wallet-generator): 🔥 Generates EVM wallets and exports mnemonic, private key, and address data to CSV.
- [wallet-tools/generate-solana-wallet](wallet-tools/generate-solana-wallet): 🌊 Generates Solana wallets and writes addresses and private key formats to separate files.
- [wallet-tools/evm-sub-wallet-generator](wallet-tools/evm-sub-wallet-generator): 🧩 Generates multiple EVM sub-wallets from one mnemonic seed.
- [wallet-tools/kaspa-wallet-generate](wallet-tools/kaspa-wallet-generate): 🪙 Generates Kaspa wallets and writes the wallet details to a text file.

## How to run each tool

### EVM wallet generator

```bash
pip install -r wallet-tools/evm-wallet-generator/requirements.txt
python wallet-tools/evm-wallet-generator/bot.py
```

Use this when you want a single wallet CSV with mnemonic and key material.

### Solana wallet generator

```bash
pip install -r wallet-tools/generate-solana-wallet/requirements.txt
python wallet-tools/generate-solana-wallet/solana.py
```

Use this when you want addresses and private keys written into separate files for Solana.

### EVM sub-wallet generator

```bash
pip install -r wallet-tools/evm-sub-wallet-generator/requirements.txt
python wallet-tools/evm-sub-wallet-generator/bot.py
```

Use this when you want many EVM wallets derived from one seed phrase.

### Kaspa wallet generator

```bash
pip install -r wallet-tools/kaspa-wallet-generate/requirements.txt
python wallet-tools/kaspa-wallet-generate/main.py
```

Use this when you want Kaspa wallet output written to a readable text file.

## Generated files

- EVM wallet generator: `evm_wallets.csv`
- Solana wallet generator: `wallet.txt`, `pvt.csv`, `pvt2.csv`
- EVM sub-wallet generator: `evm_wallets.csv`
- Kaspa wallet generator: `wallets.txt`

These generated files are ignored by git so they do not pollute commits.

## 🧭 Suggested Flow

- Read the folder README first if you only need one tool.
- Run the tool from inside its own folder when you want the output files to land there.
- Keep generated wallets out of commits unless you are intentionally sharing sample data.

## ⚠️ House Rules

- Do not clone the old standalone repos again unless you need history.
- Keep each wallet tool separate inside `wallet-tools/` so updates stay clean.
- Treat wallet output as sensitive data.

## Supporting docs

- [wallet-tools/README.md](wallet-tools/README.md): folder-level guide.
- [DELETE-REPOS.md](DELETE-REPOS.md): repos to delete after migration.
