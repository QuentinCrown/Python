# enter your grade in the ("Please enter a numeric grade (0-100)") below
grade = ( "Please enter a numeric grade (0-100)" ) 

print(f"you have {grade}%")

# is the grade between 0 and 100? lets find out
if 0 <= grade <= 100:
    # grading scale
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    print(f"Your letter grade is: {letter_grade}")
else:
    print("Invalid grade entered. Please enter a grade between 0 and 100.")
