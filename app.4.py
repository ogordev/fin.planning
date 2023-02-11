#Define end-of-year goal
end_of_year_goal = 250000

#Define monthly expenses
rent = 500
utilities = 150
food = 300
transportation = 100
entertainment = 300

#Calculate total monthly expenses
monthly_expenses = rent + utilities + food + transportation + entertainment

#Calculate monthly income
monthly_income = 7000

#Calculate monthly surplus
monthly_surplus = monthly_income - monthly_expenses

#Calculate number of months remaining in the year
from datetime import datetime
now = datetime.now()
months_remaining = 12 - now.month

#Account balance and interest rate if you up your account 10% per month
balance = 500
apm = 0.01
monthly_interest = apm

#Calculate and print monthly balance for each month until the end of the year
for i in range(months_remaining):
    interest = balance * monthly_interest
balance *= (1 + monthly_interest)
balance += monthly_surplus
monthly_earnings_goal = end_of_year_goal - balance
print("Month", i + 1, "balance: ", balance, "interest: ", interest, "Monthly additional earnings goal to attain your", end_of_year_goal,"goal : ", monthly_earnings_goal)

#Print results
print("Monthly expenses: ", monthly_expenses)
print("Monthly surplus: ", monthly_surplus)
print("Months remaining in the year: ", months_remaining)
print("That's an additional", monthly_earnings_goal / 30,"per day. Or that's an extra ", monthly_earnings_goal / 200,"hoodies sold per month if you make 200euros profits per hoodie.")
print("Time to level your hustle man!")