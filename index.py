from bs4 import BeautifulSoup
import requests
import json
import time

# Create a function to run a query on the Uniswap GraphQL API
def run_query(q):
    request = requests.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2', json={'query': q})
    if request.status_code == 200:
        return request.text
    else:
        raise Exception('Query failed. Return code is {}'.format(request.status_code))


# Create a function to use a honeypot ethereum checker
def check_honeypot(contract_address):
    r = requests.get(f'https://honeypot.is/ethereum?address={contract_address}')
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        warnings = soup.find("ul", {"class": "WARNINGS"})
        if warnings is not None:
            return True
        else:
            return False
    else:
        raise Exception(f'Error checking contract {contract_address}. Return code is {r.status_code}')

# Create a function to query Etherscan for the source code of a contract
def query_etherscan(contract_address):
    request = requests.get(f'https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey=961XF454VCYXBHA4RGTR812XI2R2GFUSJW')
    if request.status_code == 200:
        return request.text 
    else:
        raise Exception('Query failed. Return code is {}'.format(request.status_code))

# Create a function to check if a given list of functions exists in the source code of a contract
def check_exist_function(source_code, function_list):
    for function in function_list:
        if function in source_code:
            return False
    return True

# Create a function to check if a given token already exists in a list of tokens
def check_existing_token_in_list(token, token_list):
    for t in token_list:
        if t['token'] == token:
            return True
    return False

# Create a function to check if a contract is a Uniswap V2 contract
def check_holders(contract_address):
    r = requests.get(f"https://etherscan.io/token/generic-tokenholders2?a={contract_address}&s=0&p=", headers={'User-Agent': 'Mozilla/5.0'})
    html = r.text
    if 'Public Tag: Uniswap V2' in html or 'Public Tag: Null Address' in html:
        return True

# Create a function to get the latest added pairs to the Uniswap network
def get_new_tokens():
    query = """
    {
      pairs(first: 20, orderBy: createdAtTimestamp, orderDirection: desc) {
        token0 {
          id
          symbol
          totalLiquidity
          name
          totalSupply
          tradeVolumeUSD
        }
      }
    }
    """
    data = run_query(query)
    json_data = json.loads(data)
    return json_data['data']['pairs']

# Load the existing list of tokens from the tokens.json file
with open('tokens.json') as fp:
    existing_tokens = json.load(fp)

# Load the existing list of scams from the scams.json file
with open('scams.json') as fp:
    existing_scams = json.load(fp)

# Keep checking for newly tokens
while True:
    new_tokens = get_new_tokens()
    for token in new_tokens:
        total_liquidity = token['token0']['totalLiquidity']
        token_name = token['token0']['name']
        contract_address = token['token0']['id']
        symbol = token['token0']['symbol']
        if not check_existing_token_in_list(contract_address, existing_tokens):
            if check_holders(contract_address):
                source_code = query_etherscan(contract_address)
                json_source_contract = json.loads(source_code)
                full_code = json_source_contract['result'][0]['SourceCode']
                ABI = json_source_contract['result'][0]['ABI']
                CompilerVersion = json_source_contract['result'][0]['CompilerVersion']
                # Check if the source code includes any suspicious functions
                if check_exist_function(source_code, ['_TaxReduce', '_settxlimit', '_freeset', '_mint', '_flashloan', '_burn', 'deductFee', 'multiFrontListed', '_multiApprove', 'claimERC20', 'updateSellFee', 'renounceOwnership', 'SellTax', 'BlockBots', 'unblockBots', 'Transfers', 'setFees', 'maxtx', 'setBots', 'reconfigure', 'safeTransfer', 'initialize', 'setFeeAmountOne', 'approveAndCall', 'setFeeAmountTwo', 'approveSwap', '_setMaxWalletSize', '_onlyOwnes', '_allocate', 'setFeeAmountOne', 'setFeeAmountTwo', 'initial', 'approveSwap', 'approveAndCall'] or (full_code or ABI != 'Contract source code not verified') or (CompilerVersion.startswith('v0.6') or CompilerVersion.startswith('v0.8')) or not check_honeypot(contract_address)):
                    # If the source code doesn't get flagged from one of the tests, add the token to the existing list
                    existing_tokens.append({'name': token_name, 'token': contract_address, 'symbol': symbol, 'Liquitidy': total_liquidity})
                    print(f'Added new token {token_name}:{symbol} ({contract_address}) to the existing list.\n')
                else:
                    # If the source code does get flagged from one of the tests, add the token to the list of scams
                    existing_scams.append({'name': token_name, 'token': contract_address, 'symbol': symbol, 'Liquitidy': total_liquidity})
                    print(f'Added new scam {token_name}:{symbol} ({contract_address}) to the existing list.\n')
        else:
            print(f'Token {token_name}:{symbol} ({contract_address}) already exists in the list.\n')
        with open('tokens.json', 'w') as fp:
            json.dump(existing_tokens, fp, indent=4)
        with open('scams.json', 'w') as fp:
            json.dump(existing_scams, fp, indent=4)
        time.sleep(10)

