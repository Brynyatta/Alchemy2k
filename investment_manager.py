# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 15:40:01 2018

@author: Eier
"""

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
        return (investment_manager.investment);
    
            
    
    
    
    
    
    