import math                                                                                                         # Adds math functionality to the application

P = float(input("Please enter the amount you are depositing: R "))                                                  # Requests float input from user and stores as a variable / P
i = float(input("Please enter your interest rate (in %): "))                                                        # Requests float input from user and stores as a variable / i
t = float(input("Please enter the number of years of the investment: "))                                            # Requests float input from user and stores as a variable / t
interest = input("Please select your interest type (Simple or Compound): ")                                         # Requests string input from user and stores as a variable 

r = i/100                                                                                                           # Divides user entered float with 100 and stores into a variable

simpleA = round(P*(1+r*t), 2)                                                                                       # Calculates Simple interest and stores rounded solution to a variable
compoundA = round(P* math.pow((1+r),t), 2)                                                                          # Calculates Compound interest and stores rounded solution to a variable

if interest == "Simple":                                                                                            # If user selected interest type equals 'Simple', it prints simple interest calculated amount.
    print ("Your total amount will be R", simpleA, " in ", int(t), " years, at an interest rate of", i,"%")
elif interest == "Compound":                                                                                        # If user selected interest type equals 'Compound', it prints compound interest calculated amount.
    print ("Your total amount will be R", compoundA, " in ", int(t), " years, at an interest rate of", i,"%")
else :                                                                                                              # If user inputs invalid data.
    print("You have not selected a correct interest type.")

