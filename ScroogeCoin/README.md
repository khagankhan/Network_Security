# ScroogeCoin Transaction Handler

This project implements the transaction handler for the ScroogeCoin cryptocurrency. The main goal of the project is to validate transactions, prevent double-spending, and update the UTXOPool accordingly.

## Table of Contents

- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Files Provided](#files-provided)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [Testing](#testing)

## Getting Started

Clone the repository to your local machine:

`git clone https://github.com/khagankhan/Network_Security.git`

## Usage

1. Complete the implementation of `TxHandler.java`. Your implementation should be able to validate transactions and update the UTXOPool.

2. Compile and test your code: type `make`

## Implementation Details

The main task is to implement the `handleTxs` method in `TxHandler.java`. This method should return a mutually valid transaction set of maximal size and update the internal UTXOPool accordingly.

To achieve this, consider the following steps:

1. Validate the given transactions.
2. Prevent double-spending by ensuring no transaction input claims the same UTXO more than once.
3. Update the UTXOPool by removing the UTXOs claimed by the validated transactions and adding new UTXOs created by these transactions.

## Testing

You are responsible for creating your own test cases to ensure the functionality of your implementation. Test your code thoroughly to make sure it works as expected.



