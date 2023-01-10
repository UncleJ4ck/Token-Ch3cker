FIRST PHASE:
⌛️: analyzing the contract and all the function called by the dev, in some minutes it can be classified

SECOND PHASE:

You can see all of this in the source code of the smart contract

✅: the contract is verified, renonced , locked liq, no sketchy function 
⚠️: the contract has something suspicious, liq is not yet locked, not yet renounced
❌: the contract is a scam, no lock, no renounce, sketchy function


USE https://tokensniffer.com/ to check for tokens
check for liquidity lock using: https://unicrypt.network/

*check for those functions:

if you find a function that i wrote an X mark in front of it it's a scam ❌ and the vice versa 


function _TaxReduce: ❌
function _settxlimit: ❌
function _freeset: ❌
function _mint: ❌
function Modifier : owner + swap✅
function _flashloan: ❌
function multiFrontListed
function SellTax: ❌
function BlockBots / unblockBots: ❌
function Transfers: ❌
function _setMaxWalletSize: ❌
function _onlyOwnes: ❌
function _allocate:❌
function setFeeAmountOne/setFeeAmountTwo: ❌
function initial / approveSwap / approveAndCall: ❌
swapandliquify == false (it's a honeypot): ❌
unlocktime function in transactions (you need to check it and decompile it and put it in the timestamp)
funciton v2 router have 0x10/0x7 ✅
Compiler version 0.8/0.6 ✅
holder 90%==>95%  null adresse+ locked✅
wallet address == death wallet✅
teelgram link ✅ : https://web.telegram.org/k/#@vanpelt_tokenhunter

```
ID 	Pattern name 	Severity 	Slither ID 	SWC ID 	Comments
1 	TODAmount 	Critical 	- 	SWC-114 	
2 	TODReceiver 	Critical 	- 	SWC-114 	
3 	TODTransfer 	Critical 	- 	SWC-114 	
4 	UnrestrictedWrite 	Critical 	- 	SWC-124 	
5 	RightToLeftOverride 	High 	rtlo 	SWC-130 	
6 	ShadowedStateVariable 	High 	shadowing-state, shadowing-abstract 	SWC-119 	
7 	UnrestrictedSelfdestruct 	High 	suicidal 	SWC-106 	
8 	UninitializedStateVariable 	High 	uninitialized-state 	SWC-109 	
9 	UninitializedStorage 	High 	uninitialized-storage 	SWC-109 	
10 	UnrestrictedDelegateCall 	High 	controlled-delegatecall 	SWC-112 	
11 	DAO 	High 	reentrancy-eth 	SWC-107 	
12 	ERC20Interface 	Medium 	erc20-interface 	- 	
13 	ERC721Interface 	Medium 	erc721-interface 	- 	
14 	IncorrectEquality 	Medium 	incorrect-equality 	SWC-132 	
15 	LockedEther 	Medium 	locked-ether 	- 	
16 	ReentrancyNoETH 	Medium 	reentrancy-no-eth 	SWC-107 	
17 	TxOrigin 	Medium 	tx-origin 	SWC-115 	
18 	UnhandledException 	Medium 	unchecked-lowlevel 	- 	
19 	UnrestrictedEtherFlow 	Medium 	unchecked-send 	SWC-105 	
20 	UninitializedLocal 	Medium 	uninitialized-local 	SWC-109 	
21 	UnusedReturn 	Medium 	unused-return 	SWC-104 	
22 	ShadowedBuiltin 	Low 	shadowing-builtin 	- 	
23 	ShadowedLocalVariable 	Low 	shadowing-local 	- 	
24 	CallToDefaultConstructor? 	Low 	void-cst 	- 	
25 	CallInLoop 	Low 	calls-loop 	SWC-104 	
26 	ReentrancyBenign 	Low 	reentrancy-benign 	SWC-107 	
27 	Timestamp 	Low 	timestamp 	SWC-116 	
28 	AssemblyUsage 	Info 	assembly 	- 	
29 	ERC20Indexed 	Info 	erc20-indexed 	- 	
30 	LowLevelCalls 	Info 	low-level-calls 	- 	
31 	NamingConvention 	Info 	naming-convention 	- 	
32 	SolcVersion 	Info 	solc-version 	SWC-103 	
33 	UnusedStateVariable 	Info 	unused-state 	- 	
34 	TooManyDigits 	Info 	too-many-digits 	- 	
35 	ConstableStates 	Info 	constable-states 	- 	
36 	ExternalFunctions 	Info 	external-function 	- 	
37 	StateVariablesDefaultVisibility 	Info 	- 	SWC-108 
``` vulnerabilities to add 

and check this website to check: https://dasp.co/


add a token sniffer api scanner: https://honeypot.is/ethereum

supporting other decentralized exchange protocols

-    0x: 0x is a decentralized exchange protocol that uses Ethereum smart contracts to facilitate trades. It allows users to trade ERC-20 tokens directly with one another, without the need for a traditional centralized exchange.

-    Kyber Network: Kyber Network is a decentralized exchange protocol that allows users to buy and sell Ethereum tokens directly with one another. It uses a reserve system to provide liquidity and facilitate trades.

-    Bancor: Bancor is a decentralized exchange protocol that uses smart contracts to allow users to buy and sell Ethereum tokens directly with one another. It uses a reserve system to provide liquidity and facilitate trades.

-    AirSwap: AirSwap is a decentralized exchange protocol that uses a peer-to-peer model to allow users to buy and sell Ethereum tokens directly with one another. It uses a "request for quote" model to facilitate trades.