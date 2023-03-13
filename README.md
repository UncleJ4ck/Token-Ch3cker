# Token-Ch3ker

a monitoring tool to check for new tokens that are added to the Uniswap DeFi and determine whether they are a scam or not. It does this by using different online APIs such as the Uniswap GraphQL API, honeypot.is, and Etherscan. 

## Chapter 1: What's a DeFi ??

DeFi, or decentralized finance, is a new way of providing financial services using blockchain technology. Instead of relying on traditional institutions like banks, DeFi uses smart contracts and other blockchain-based tools to create a more open and accessible financial system. This means that anyone with an internet connection can use these services, regardless of where they are located or what their financial status is. Some popular examples of DeFi services include lending and borrowing money, trading cryptocurrencies, and buying insurance. The idea behind DeFi is to create a financial system that is more open, fair, and accessible to everyone.

## Chapter 2: Uniswap Why Uniswap ? how is it related to Ethereum

Uniswap is a decentralized exchange protocol that lets people trade cryptocurrencies without needing a bank or other middleman. Instead, it uses something called a "smart contract" on the Ethereum blockchain to make sure that trades happen automatically and fairly. This means that trading is faster, cheaper, and more private than on other websites.

> Everything is under ERC-20 

# Installation

```
git clone https://github.com/UncleJ4ck/Token-Ch3ker
cd Token-Ch3ker
pip install -r requirements.txt
```

## Docker

```docker
docker build -t token-ch3ker:latest .
docker run --rm -it --name checker token-ch3ker
```

# Usage
```
python3 index.py
```
> and wait for results, you will find the results in the json files

# TO-DO

- [x] Adding a honeypot checker
- [ ] Keep updating the rules of checking
- [ ] Creating a vulnerability scanner for smart contract (better than keep adding rules to check)
