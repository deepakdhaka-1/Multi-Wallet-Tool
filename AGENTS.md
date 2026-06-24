# Agent Guide

This repository is a flattened wallet-tools workspace. Each tool lives in its own top-level folder.

## Folder map

- `evm-wallet-generator/`: generates EVM wallets and exports CSV output.
- `generate-solana-wallet/`: generates Solana wallets and writes address/key files.
- `evm-sub-wallet-generator/`: generates multiple EVM wallets from one mnemonic seed.
- `kaspa-wallet-generate/`: generates Kaspa wallets and writes wallet details to a text file.

## Common commands

```bash
pip install -r evm-wallet-generator/requirements.txt
python evm-wallet-generator/bot.py
```

```bash
pip install -r generate-solana-wallet/requirements.txt
python generate-solana-wallet/solana.py
```

```bash
pip install -r evm-sub-wallet-generator/requirements.txt
python evm-sub-wallet-generator/bot.py
```

```bash
pip install -r kaspa-wallet-generate/requirements.txt
python kaspa-wallet-generate/main.py
```

## Repo rules

- Keep generated wallet files out of commits.
- Keep each tool independent inside its own folder.
- Treat wallet output as sensitive data.
- Update the root README when adding or removing tools.
