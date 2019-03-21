class trader(object):

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def invest(self,investment):
        if investment > self.balance:
            print("Insuff'icient funds!")
            return 0;
        else:
            self.balance -= investment
            return investment;
        
    
    def profit(self,profitvalue):
        self.balance += profitvalue
        
def investment_manager(change,shorted):
    
    # Input variables
    initial_investment = 10000
    shorting_allowed = True
    
    if investment_manager.counter == 0:
        investment_manager.investment = initial_investment
    investment_manager.counter += 1
    
    
    if shorted == 1 and shorting_allowed == False:
        return investment_manager.investment;
    else:
        investment_manager.investment += change
        return (investment_manager.investment);s