# Wallet Tools

This folder groups the wallet repos that now live inside the consolidated workspace.

## 🚪 Entry Point

Start here when you want the fast mental map for the wallet tools area.

## Contents

```text
wallet-tools/
  evm-wallet-generator/
  generate-solana-wallet/
  evm-sub-wallet-generator/
  kaspa-wallet-generate/
```

## Purpose

- `evm-wallet-generator`: 🔥 EVM wallet generation and CSV export.
- `generate-solana-wallet`: 🌊 Solana wallet generation and file export.
- `evm-sub-wallet-generator`: 🧩 EVM sub-wallet generation from a single mnemonic.
- `kaspa-wallet-generate`: 🪙 Kaspa wallet generation with Bech32m output.

## Notes

- Each tool keeps its own README and entrypoint so the repos stay easy to run independently.
- Copy new source updates into the matching folder before deleting the standalone upstream repo.
- Generated wallet files are ignored by git at both the root and folder level.