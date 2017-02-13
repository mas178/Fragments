"""
Transaction
Transactionには、メッセージをやり取りするMessageTransactionと価値をやり取りするFeeTransactionの２種類がある.
"""


class Transaction:
    def __init__(self, counter_party: 'User') -> None:
        self.counter_party = counter_party


class MessageTransaction(Transaction):
    def __init__(self, counter_party: 'User', msg: str, fee: float) -> None:
        Transaction.__init__(self, counter_party)
        self.msg = msg
        self.fee = fee

    def __str__(self) -> str:
        return 'Message Transaction: "{msg}" to {counter_party} with fee {fee}'.format(msg=self.msg, counter_party=self.counter_party, fee=self.fee)


class FeeTransaction(Transaction):
    def __init__(self, counter_party: 'User', value: float) -> None:
        Transaction.__init__(self, counter_party)
        self.value = value

    def __str__(self) -> str:
        return 'Fee Transaction: {counter_party} gets confirmation fee {value}'.format(counter_party=self.counter_party, value=self.value)


class SignedTransaction:
    def __init__(self, trx: Transaction, signer: 'User') -> None:
        self.trx = trx
        self.signer = signer

    def __str__(self) -> str:
        return 'Transaction signed by {signer} ({trx})'.format(signer=self.signer, trx=self.trx)
