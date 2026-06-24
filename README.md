# Multi Wallet Tools

This repo contains four wallet tools. Each one lives in its own top-level folder, so you can open the tool you want and run it directly.

## Folders

- [evm-wallet-generator](evm-wallet-generator): creates EVM wallets.
- [generate-solana-wallet](generate-solana-wallet): creates Solana wallets.
- [evm-sub-wallet-generator](evm-sub-wallet-generator): creates multiple EVM wallets from one seed.
- [kaspa-wallet-generate](kaspa-wallet-generate): creates Kaspa wallets.

## How to use

1. Open the folder for the tool you want.
2. Install the requirements file inside that folder.
3. Run the Python file inside that folder.

### Example

```bash
pip install -r evm-wallet-generator/requirements.txt
python evm-wallet-generator/bot.py
```

## Output files

- EVM wallet generator: `evm_wallets.csv`
- Solana wallet generator: `wallet.txt`, `pvt.csv`, `pvt2.csv`
- EVM sub-wallet generator: `evm_wallets.csv`
- Kaspa wallet generator: `wallets.txt`

## Notes for agents

Read [AGENTS.md](AGENTS.md) first if you need the repo map or run commands.
Generated wallet files are ignored by git.
