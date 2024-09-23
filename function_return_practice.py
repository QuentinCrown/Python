# interest setup
def calculate_interest(principal, rate, time):
    # interest formula
    interest = (principal * rate * time) / 100
    return interest

# enter you information in the " " below
principal_amount = float((" ")) #money
interest_rate = float((" ")) #percentage
investment_time = float((" ")) #years

# interest function
calculated_interest = calculate_interest(principal_amount, interest_rate, investment_time)

# results
print(f"The simple interest for a principal amount of ${principal_amount:,.2f} "
      f"at an interest rate of {interest_rate}% over a period of "
      f"{investment_time} years is: ${calculated_interest:,.2f}")
