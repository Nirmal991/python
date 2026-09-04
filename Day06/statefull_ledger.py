AUDIT_TRANSACTION_COUNT = 0
def create_bank_account(owner_name, initial_bal):
    balance  = float(initial_bal)
    history = [f'Acc create with {balance}']
    def deposit(amt):
        nonlocal balance
        global AUDIT_TRANSACTION_COUNT

        balance += amt
        history.append(f"deposit {amt}")
        AUDIT_TRANSACTION_COUNT += 1

    def withdraw(amt):
        nonlocal balance
        global AUDIT_TRANSACTION_COUNT

        if balance >= amt:
            balance -= amt
            history.append(f"withdraw {amt}")
            AUDIT_TRANSACTION_COUNT += 1
        else:
            raise ValueError(f"Insufficient balance")

    def get_statment():
        return(
            owner_name,
            balance,
            history.copy()
        )
    return {
        "deposit" : deposit,
        "withdraw" : withdraw,
        "statement" : get_statment
    }

def main():
    print(AUDIT_TRANSACTION_COUNT)

    acc = create_bank_account("Arham", 1000.0)

    acc["deposit"](200.0)

    acc["withdraw"](150.0)

    try:
        acc["withdraw"](2000.0)
    except ValueError as e:
        print(e)

    # Get statement
    owner, bal, txn_history = acc["statement"]()

    print(owner)
    print(bal)
    print(txn_history)

    # Verify global log count
    print(AUDIT_TRANSACTION_COUNT)



main()