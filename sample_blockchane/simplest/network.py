from simplest.transaction import SignedTransaction
from simplest.user import User


class Network:
    def __init__(self):
        self.users = set([])

    def add(self, user: User) -> None:
        self.users.add(user)

    def announce_signed_trx(self, signed_trx: SignedTransaction) -> None:
        print('[Network.announce_signed_trx] announcing "{}"'.format(signed_trx))
        for user in self.users:
            user.receive_signed_trx(signed_trx)

    def announce_block(self, block: 'Block') -> None:
        print('[Network.announce_block] announcing "{}"'.format(block))
        for user in self.users:
            user.receive_block(block)

    @staticmethod
    def validate_block_id(block_id: str) -> bool:
        return block_id.startswith('000')
