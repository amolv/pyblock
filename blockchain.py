# empty list available in global scope
blockchain = []

def get_last_blockchain_value():
    """ Return last value of current blockchain """
    return blockchain[-1]

def add_value( transaction_amount, last_transaction = [1]  ):
    """Append new value to blockchain
    Arguments:
    :Txn : txn amount
    :last_t : last txn default [1]
    """
    blockchain.append([ last_transaction, transaction_amount ])    

def get_user_input():
    return input('Enter txn amount:')    

txn_amount = get_user_input()
# optinal argument
add_value( txn_amount )

txn_amount = get_user_input()
# kwards arguments 
add_value( last_transaction = get_last_blockchain_value() , transaction_amount = txn_amount )

txn_amount = get_user_input()
add_value( txn_amount, get_last_blockchain_value() )

print( blockchain)