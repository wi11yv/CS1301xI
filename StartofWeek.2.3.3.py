value = 100
quantity = 5
interest = 0.02
dividend = 1.05
dividend_frequency = 4
years = 10
goal = 250

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Typically when you purchase a stock on the stock market, you
#do so with the hope that it will increase in value, and you
#can then sell it for a profit.
#
#Some stocks also pay dividends. A dividend is a small amount
#of money that a stock pays its owners on a regular interval.
#For example, if a stock pays a $1.05 dividend 4 times a year,
#then for each share of the stock you own, you would receive
#$4.20 per year.
#
#The variables above give a number of parameters for a
#particular stock purchase you are considering:
#
# - value, the current value of the stock
# - quantity, the number of shares you may buy
# - interest, the estimated yearly interest rate it will earn
# - dividend, the predicted value of the dividend it will pay
# - dividend_frequency, the predicted frequency with which it
#   will pay that dividend
# - years, the number of years you plan to hold the stock
# - goal, the amount of money you want to earn from the
#   investment
#
#Your goal is to print True if this investment will meet your
#savings goal, and False if it will not. In other words, if
#the total amount of money you will earn from the stock --
#including its initial value, interest, and dividends -- is
#greater than goal, you print True. Otherwise, you print False.
#
#You can find the total amount of money generated by dividends
#by multiplying the dividend by its yearly frequency by the
#number of years.
#
#The formula for the current value of an investment based on
#its initial value, its interest rate, and its years of investment
#is:
#
# new value = initial value * e ^ (interest rate * number of years)
#
#The variable interest can be put directly into this formula (you
#do not need to add 1). The following line of code will let you use
#the variable e in your code for e:
from math import e

#Remember, your only goal is to print True if you should buy the
#stock, False if you should not. Using the initial values of the
#variables above, this would initially print False: the total
#value would be around $164, well short of the goal of $250.


#Add your code here!

new_value = (value * e ** (interest * years)) + (dividend * dividend_frequency * years)
print(new_value > goal)
