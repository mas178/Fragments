from simplest.transaction import Transaction, MessageTransaction, SignedTransaction
from simplest.verifier import Verifier


class User(Verifier):
    def __init__(self, name: str, network: 'Network'):
        Verifier.__init__(self)
        print('[User.init] {name}: joining the block chain network'.format(name=name))
        network.add(self)
        self.name = name
        self.network = network

    def send(self, message: str, to: 'User', fee: float) -> SignedTransaction:
        print('\n[User.send] {name}: sending a message to {to}. ({message}:{fee}).'.format(name=self.name, to=to.name, message=message, fee=fee))
        trx = MessageTransaction(to, message, fee)
        signed_trx = self.sign(trx)
        self.network.announce_signed_trx(signed_trx)
        return signed_trx

    # these two methods should in a real world be implemented with private/public key pairs with PKI
    def sign(self, tx: Transaction) -> SignedTransaction:
        return SignedTransaction(tx, self)

    def open(self, signed_trx: SignedTransaction) -> Transaction:
        return signed_trx.trx

    def __str__(self) -> str:
        return self.name
