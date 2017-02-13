from simplest.network import Network
from simplest.user import User

network = Network()

alice = User('Alice', network)
bob = User('Bob', network)
chris = User('Chris', network)
dan = User('Dan', network)

alice.send('Yo!', to=bob, fee=1.0)
bob.send('Ho!', to=chris, fee=2.0)
chris.send('Yo!Ho!', to=alice, fee=3.0)

alice.verify_message_trxs()
dan.verify_message_trxs()
chris.verify_message_trxs()
