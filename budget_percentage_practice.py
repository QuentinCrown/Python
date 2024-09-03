# this program will calculate the percentage breakdown of your monthly budget and clearly display it to you
# you dont need to do anything here
def calculate_percentage(amount, total_budget):
    return (amount / total_budget) * 100

# now start by replacing ("total budget") with your total available budget
def main():
    total_budget = ("total budget")

    # now enter the amounts spent in each different category
    #do not use special characters, such as (,) and ($) and (.)
    housing = ("housing budget") #replace ("housing budget") with actual amount
    utilities = ("utility budget") #replace ("utility budget") with actual amount
    groceries = ("grocery budget") #replace ("grocery budget") with actual amount
    transportation = ("transport budget") #replace ("transport budget") with actual amount
    health_care = ("health care budget") #replace ("health care budget") with actual amount
    personal_care = ("personal care budget") #replace ("personal care budget)" with actual amount
    clothing = ("clothing budget") #replace ("clothing budget") with actual amount
    debt = ("debt budget") #replace ("debt budget") with actual amount

    # this will calculate the percentage of the budget for each category
    # you dont need to do anything here
    housing_percentage = calculate_percentage(housing, total_budget)
    utilities_percentage = calculate_percentage(utilities, total_budget)
    groceries_percentage = calculate_percentage(groceries, total_budget)
    transportation_percentage = calculate_percentage(transportation, total_budget)
    health_care_percentage = calculate_percentage(health_care, total_budget)
    personal_care_percentage = calculate_percentage(personal_care, total_budget)
    clothing_percentage = calculate_percentage(clothing, total_budget)
    debt_percentage = calculate_percentage(debt, total_budget)

    # this "print" function will show you your breakdowns with percentages in an easy to read format
    # you dont need to do anything here
    print("\n--- Budget Breakdown ---")
    print(f"Housing: ${housing:.2f} ({housing_percentage:.2f}%)")
    print(f"Utilities: ${utilities:.2f} ({utilities_percentage:.2f}%)")
    print(f"Groceries: ${groceries:.2f} ({groceries_percentage:.2f}%)")
    print(f"Transportation: ${transportation:.2f} ({transportation_percentage:.2f}%)")
    print(f"Health Care: ${health_care:.2f} ({health_care_percentage:.2f}%)")
    print(f"Personal Care: ${personal_care:.2f} ({personal_care_percentage:.2f}%)")
    print(f"Clothing: ${clothing:.2f} ({clothing_percentage:.2f}%)")
    print(f"Debt: ${debt:.2f} ({debt_percentage:.2f}%)")


# this will just make sure the program runs successfully
# you dont need to do anything here
if __name__ == "__main__":
    main()