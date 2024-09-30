# unit conversion
POUNDS_TO_KG = 0.453592  
INCHES_TO_METERS = 0.0254 

def main():

    while True:
        try:
            weight_pounds = float(" ") # enter your weight in pounds
            if weight_pounds <= 0:
                print("Weight must be a positive value. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for weight.")

    while True:
        try:
            height_inches = float(" ") # enter your height in inches
            if height_inches <= 0:
                print("Height must be a positive value. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for height.")

    # conversion to metric units
    weight_kg = weight_pounds * POUNDS_TO_KG
    height_meters = height_inches * INCHES_TO_METERS

    # bmi Calculation
    bmi = weight_kg / (height_meters ** 2)

    # two decimal places
    print(f"Your BMI is: {bmi:.2f}")

    # BMI Categories
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"Based on your BMI, you are categorized as: {category}")

# Run main
if __name__ == "__main__":
    main()
