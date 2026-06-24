# Agent Guide

This repository is a flattened wallet workspace. Each tool lives in its own top-level folder, and the root README is the beginner-friendly entry point.

## Map

- `evm-wallet-generator/`: creates EVM wallets and exports CSV output.
- `generate-solana-wallet/`: creates Solana wallets and writes address/key files.
- `evm-sub-wallet-generator/`: creates multiple EVM wallets from one mnemonic seed.
- `kaspa-wallet-generate/`: creates Kaspa wallets and writes wallet details to a text file.

## Run commands

### EVM wallet generator

```bash
pip install -r evm-wallet-generator/requirements.txt
python evm-wallet-generator/bot.py
```

### Solana wallet generator

```bash
pip install -r generate-solana-wallet/requirements.txt
python generate-solana-wallet/solana.py
```

### EVM sub-wallet generator

```bash
pip install -r evm-sub-wallet-generator/requirements.txt
python evm-sub-wallet-generator/bot.py
```

### Kaspa wallet generator

```bash
pip install -r kaspa-wallet-generate/requirements.txt
python kaspa-wallet-generate/main.py
```

## Working rules

- Keep generated wallet files out of commits.
- Treat wallet output as sensitive data.
- Keep each tool independent inside its own folder.
- Prefer root README updates when folder names, commands, or outputs change.
- Use the folder README for tool-specific usage details.

## What to avoid

- Do not reintroduce the removed `wallet-tools/` wrapper folder.
- Do not point docs back to the old standalone GitHub clone paths.
- Do not commit generated CSV, TXT, or cache files.
