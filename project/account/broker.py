class trader(object):

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    # Invest command, either returns amount of funds invested upon success, or
    # zero if the command failed.
    
    def invest(self,investment):
        if investment > self.balance:
            print("Insufficient funds!")
            return 0;
        else:
            self.balance -= investment
            return investment;
        
    
    def profit(self,profitvalue):
        self.balance += profitvalue
