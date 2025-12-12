from abc import ABC, abstractmethod
class PaymentSystem(ABC):
    @abstractmethod
    def authorize(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def refund(self):
        pass

class PayPal(PaymentSystem):
    def authorize(self):
        print("PayPal authorization complete.")
    def process(self):
        print("PayPal payment processed.")
    def refund(self):
        print("PayPal refund completed.")
class KaspiPay(PaymentSystem):
    def authorize(self):
        print("Kaspi: authorization done.")
    def process(self):
        print("Kaspi: payment successful.")
    def refund(self):
        print("Kaspi: refund returned.")
class VisaPayment(PaymentSystem):
    def authorize(self):
        print("Visa: card authorization successful.")

    def process(self):
        print("Visa: payment processed.")

    def refund(self):
        print("Visa: refund issued.")

if __name__ == "__main__":
    systems = [PayPal(), KaspiPay(), VisaPayment()]
    for s in systems:
        s.authorize()
        s.process()
        s.refund()
        print()