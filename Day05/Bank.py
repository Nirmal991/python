class AccountNotFoundError(Exception):
    def __init__(self, accountId):
        self.accountId = accountId
        print(f'{accountId} not found')

class OverdraftError(Exception):
    def __init__(self, with_amt, balance):
        self.with_amt = with_amt
        self.balance = balance
        print(f'{with_amt} amount exceeds the account {balance}')

class InvalidTransactionError(Exception):
    ...

def process_transaction_batch(accounts, batch_list, log_path):
    
