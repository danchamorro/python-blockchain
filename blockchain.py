blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    return None if len(blockchain) < 1 else blockchain[-1]


def add_transaction(transaction_amount, last_transaction=None):
    """ Append a new value as well as the last blockchain value to the blockchain."""
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    return float(input('Your transaction amount please: '))


def get_user_choice():
    """ The function displays the menu of choices for the user and gets a validated choice from the user."""
    return input('Your choice: ')


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)


def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False otherwise."""
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print('Invalid blockchain!')
        break

print('Done!')
