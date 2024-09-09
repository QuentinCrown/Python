# enter two integers below
num1 = (  )
num2 = (  )

print(f"the numbers are {num1} and {num2}")

# and
and_1 = (num1 > 0 and num2 > 0)
print(f"Both {num1} and {num2} are positive: {and_1}")

and_2 = (num1 < 100 and num2 < 100)
print(f"Both {num1} and {num2} are less than 100: {and_2}")

# or
or_1 = (num1 % 2 == 0 or num2 % 2 == 0)
print(f"At least one of {num1} or {num2} is even: {or_1}")

or_2 = (num1 > 50 or num2 > 50)
print(f"Either {num1} or {num2} are above 50: {or_2}")

# not
not_1 = not(num1 == num2)
print(f"{num1} and {num2} are not equal: {not_1}")

not_2 = not(num1 < 0 or num2 < 0)
print(f"Neither {num1} nor {num2} is negative: {not_2}")
