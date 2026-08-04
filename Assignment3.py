class UPI:
    def pay(self):
        print("Payment by UPI")


class CreditCard:
    def pay(self):
        print("Payment by Credit Card")


class DebitCard:
    def pay(self):
        print("Payment by Debit Card")


class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def start(self):
        self.strategy.pay()


t = Payment(UPI())
t.start()

t = Payment(CreditCard())
t.start()

t = Payment(DebitCard())
t.start()
