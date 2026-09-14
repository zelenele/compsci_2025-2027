class Transaction:
    def __init__(self, Amount, Time, Service):
        self.Amount = Amount
        self.Time = Time
        self.Service = Service
    
    def Summing(self):
        return {self.Amount, self.Time, self.Service}
class Expense(Transaction):
    transaction_type = "expense"

class Earning(Transaction):
    transaction_type = "earning"


Class 
