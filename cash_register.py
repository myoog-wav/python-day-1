'''
summing price of each item, applying discounts, calculating sales tax, 
finding the amount of chanhe to give customes who pay in cash
'''

'''
task: calculate sales tax
name: calc_sales_tax
input: tax_rate, order_total
side effect: none
return: tax
'''

def calc_sales_tax(tax_rate, order_total):
    tax = tax_rate * order_total
    return tax

