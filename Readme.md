# Fetch Token Holders

In this project, there is a Python script called `getTokenHolders.py` to retrieve the holders of a token. The script uses the Ankr RPC API to fetch the token holders and saves them to a file named `holders.json`.

## Usage Instructions

1. Navigate to the project folder:

```bash
cd get-token-holders
```

2. Create and edit the `.env` file. The file should have the following contents:

```bash
TokenAddress=<token_contract_address>
Chain=<network>
```


Replace `<token_contract_address>` with the contract address of the token and `<network>` with the desired network. Supported networks include 'arbitrum', 'avalanche', 'bsc', 'eth', 'fantom', 'polygon', 'polygon_zkevm', 'syscoin', 'optimism', 'eth_goerli', 'polygon_mumbai', and 'avalanche_fuji'.

3. Install the required dependencies:

```bash
pip install requests
pip install python-dotenv
```

4. Run the `getTokenHolders.py` script:

```bash
python getTokenHolders.py
```


This command will fetch the token holders and save them to the `holders.json` file.

5. Check the results:

The holders will be stored in the `holders.json` file. You can use this file to retrieve the relevant data.

---

Note: The `.env` file should be located in the project's root directory. Also, make sure that the `getTokenHolders.py` script includes the `load_dotenv()` function to load the `.env` file.

* Supported Networks : 

    * Arbitrum
    * Avalanche
    * BSC
    * ETH
    * Fantom
    * Polygon
    * Polygon ZK-EVM
    * Syscoin
    * Optimism
    * ETH Goerli
    * Polygon Mumbai
    * Avalanche Fuji
  
- [ 'arbitrum', 'avalanche', 'bsc', 'eth', 'fantom', 'polygon', 'polygon_zkevm', 'syscoin', 'optimism', 'eth_goerli', 'polygon_mumbai', 'avalanche_fuji']



