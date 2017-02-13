from simplest.transaction import Transaction, FeeTransaction, SignedTransaction


class Verifier:
    def __init__(self):
        self.__last_block = None
        self.__unconfirmed_trxs = []
        self.name = None
        self.network = None

    def open(self, signed_trx: SignedTransaction) -> Transaction:
        pass

    def sign(self, tx: Transaction) -> SignedTransaction:
        pass

    def receive_signed_trx(self, signed_trx: SignedTransaction) -> None:
        trx = self.open(signed_trx)
        if trx is None:
            print('[Verifier.receive_signed_trx] {name}: received invalid transaction {signed_trx}'.format(name=self.name, signed_trx=signed_trx))
            return
        if signed_trx.signer == self or trx.counter_party == self:
            print('[Verifier.receive_signed_trx] {name}: not going to verify this transaction as I\'m involved'.format(name=self.name))
            return
        self.__unconfirmed_trxs.append(signed_trx)
        print('[Verifier.receive_signed_trx] {name}: unconfirmed transactions {unconfirmed_trxs}'.format(
            name=self.name, unconfirmed_trxs=self.__unconfirmed_trxs))

    def receive_block(self, block: 'Block') -> None:
        # validate block
        if not block.validate():
            print('[Verifier.receive_block] {name}: !!! invalid {block} is found !!!'.format(name=self.name, block=block))
            return

        print('[Verifier.receive_block] {name}: validated {block} is valid'.format(name=self.name, block=block))
        self.__last_block = block

        # if a transaction is already confirmed in a given block, remove it from unconfirmedTxs
        self.__unconfirmed_trxs = list(set(self.__unconfirmed_trxs).difference(set(block.trxs)))
        for signed_trx in [trx for trx in block.trxs if trx.signer == self]:
            print('[Verifier.receive_block] {name}: my trx "{trx}" is validated by network!'.format(name=self.name, trx=self.open(signed_trx)))

    def verify_message_trxs(self) -> None:
        # TODO: verify no double spend
        total_fee = sum([self.open(trx).fee for trx in self.__unconfirmed_trxs])

        fee_trx = FeeTransaction(self, total_fee)
        encrypted = self.sign(fee_trx)
        print('\n[Verifier.verify_message_trxs] {name}: created {encrypted}'.format(name=self.name, encrypted=encrypted))
        from simplest.block import Block
        self.__unconfirmed_trxs.append(encrypted)
        block = Block(self.__unconfirmed_trxs, self.__last_block)
        self.__unconfirmed_trxs = []

        self.network.announce_block(block)
