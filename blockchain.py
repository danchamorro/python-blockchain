blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=None):
    """ Append a new value as well as the last blockchain value to the blockchain."""
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a float. """
    return float(input('Your transaction amount please: '))


# Get the first transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(tx_amount)

# Get the second transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

# Get the third transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

# Output the blockchain list to the console
print(blockchain)
