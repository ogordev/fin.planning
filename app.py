# Define end-of-year goal
end_of_year_goal = 250000

# Define monthly expenses
rent = 500
utilities = 150
food = 300
transportation = 100
entertainment = 300

# Calculate total monthly expenses
monthly_expenses = rent + utilities + food + transportation + entertainment

# Calculate monthly income
monthly_income = 7000

# Calculate monthly surplus
monthly_surplus = monthly_income - monthly_expenses

# Calculate number of months remaining in the year
from datetime import datetime
now = datetime.now()
months_remaining = 12 - now.month

# Calculate amount needed to earn each month to reach end-of-year goal
monthly_earnings_goal = (end_of_year_goal - (monthly_surplus * months_remaining)) / months_remaining

# Account balance and interest rate
#balance = 500
#apr = 0.055
#monthly_interest = apr / 12

# Account balance and interest rate if you up your account 10% per month
balance = 500
apm = 0.01
monthly_interest = apm

# Account balance and interest rate if you up your account 10% per day
#balance = 500
#apd = 0.1
#monthly_interest = apd ** 30

    
# Calculate and print monthly balance for each month until the end of the year
for i in range(months_remaining):
    interest = balance * monthly_interest
    balance *= (1 + monthly_interest)
    balance += monthly_surplus
    print("Month", i + 1, "balance: ", balance, "interest: ", interest)
    
# Print results
print("Monthly expenses: ", monthly_expenses)
print("Monthly surplus: ", monthly_surplus)
print("Months remaining in the year: ", months_remaining)
print("Monthly additional earnings goal to attain your", end_of_year_goal,"goal : ", monthly_earnings_goal)
print("That's an additional", monthly_earnings_goal / 30,"per day. Or that's an extra ", monthly_earnings_goal / 200,"hoodies sold per month if you make 200euros profits per hoodie.")
print("Time to level your hustle man!")