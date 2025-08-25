# Name: Nhan Nguyen
# Filename: deans_honor_checker.py
# Desciption: This program checks if a student qualifies for the Dean's List or Honor Roll based on their GPA.

lastname = input("Enter your last name: ")
if lastname.lower() == "zzz":
    print("Invalid last name")
    exit()

firstname = input("Enter your first name: ")
score = float(input("Enter your GPA: "))

if score >= 3.5:
    print("Congratulations, you are in the Deans List!")
elif score >= 3.25:
    print("Congratulations, you are on the Honor Roll!")
else:
    print("You did not make the Dean's List or Honor Roll.")
