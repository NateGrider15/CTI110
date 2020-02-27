# Sales prediciton based on fact that annual profit is typically 23% of total sales
# 02/18/20
# CTI-110 P2T1 - Sales Prediction
# Nathan Grider
#

total_sales = float(input('Enter the projected sales: '))
profit = total_sales * 0.23
print('The profit is $', format(profit, '.2f'))
