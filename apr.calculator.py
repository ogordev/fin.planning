# Calculate number of months remaining in the year
from datetime import datetime
now = datetime.now()
months_remaining = 12 - now.month

# Account balance and interest rate
balance = 5000
apr = 0.055
monthly_interest = apr / 12

# Calculate and print monthly balance for each month until the end of the year
for i in range(months_remaining):
    balance += balance * monthly_interest
    print("Month", i + 1, "balance: ", balance)