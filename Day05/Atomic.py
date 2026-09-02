from copy import deepcopy

class AccountNotFoundError(Exception):
    def __init__(self, accId):
        self.accId = accId
        super().__init__(f"Account not found with {accId}")

class OverdraftError(Exception):
    def __init__(self, acc, balance, with_amt):
        self.acc = acc
        self.with_amt = with_amt
        self.balance = balance
        super().__init__(
            f"Insufficient funds. Account {acc} has balance "
            f"{balance}, requested {with_amt}."
        )

class InvalidTransactionError(Exception):
    def __init__(self, message):
        super().__init__(message)

def process_transaction_batch(accounts, batch_list, log_path):
    curr_acc = deepcopy(accounts)

    try:
        for trans in batch_list:
            acc = trans["acc"]
            trans_type = trans["type"]
            amt = trans["amt"]

            if acc not in accounts:   # her eaccounts key are checked
                raise AccountNotFoundError(acc)

        if trans_type not in ("deposit", "withdraw"):
            raise InvalidTransactionError(
                f"Invalid trans_type {trans_type}"
            )

        if amt <= 0:
            raise InvalidTransactionError(
                f"Amount is 0"
            )

        if trans_type == "deposit":
            accounts[acc] += amt

        elif trans_type == "withdraw":

            if accounts[acc] < amt:
                raise OverdraftError(acc, accounts[acc], amt)
            accounts[acc] -= amt

        with open(log_path, "a") as file:
            file.write(
                f"[SUCCESS] Batch Completed. "
                f"{len(batch_list)} trabsactions completed.\n"
           )

        return accounts
        
    except Exception as e:
        accounts.clear()
        accounts.update(curr_acc)


        with open(log_path, "a") as file:
            file.write(
                f"[ROLLBACK] batch aborted: "
                f"{type(e).__name__} - {e}\n"
            )

        raise
        

    