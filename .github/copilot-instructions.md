# Copilot Instructions

This repository contains four wallet tools at the top level. Use the root README for a beginner summary and this file for Copilot-friendly repo guidance.

## Repo map

- `evm-wallet-generator/`: EVM wallet CLI.
- `generate-solana-wallet/`: Solana wallet generator.
- `evm-sub-wallet-generator/`: EVM sub-wallet generator.
- `kaspa-wallet-generate/`: Kaspa wallet generator.

## Editing rules

- Keep the flattened folder structure.
- Update the top-level README when a path, command, or folder changes.
- Keep each tool self-contained inside its own folder.
- Do not add generated wallet output to source control.

## Run examples

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

## Safety

- Treat wallet material as sensitive.
- Avoid broad refactors unless the user asks for them.
- Prefer minimal, path-correct edits.