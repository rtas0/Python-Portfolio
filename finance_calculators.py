# import math
import math

# user chooses investment or bond, ensure it is in lowercase
requested_action = (input("""Please choose either 'bond' or 'investment from the below menu to proceed:
                       
                       bond - to calculate the amount you'll have to pay on a home loan
                       investment - to calculate the amount of interest you'll earn on your investment""")).lower()

if requested_action == "bond":
    # ask user for necessary inputs for a bond
    current_house_value = int(input("What is the current worth of the house in £?"))
    bond_interest_rate = float(input("What is the current interest rate in %?"))/1200
    repayment_length = int(input("How many months are you taking to repay the bond?"))
    # calculate monthly repayment for a bond
    monthly_repayment = int((bond_interest_rate * current_house_value)/(1 - (1 + bond_interest_rate)**(-repayment_length)))
    print("You will have to repay £" + str(monthly_repayment) + " per month")

elif requested_action == "investment":
    # ask user for necessary inputs for an investment
    deposit = int(input("How much money in £ is being deposited?"))
    investment_interest_rate = float(input("What annual interest rate are you receiving in %"))/100
    deposit_length = int(input("How many years are you investing for?"))
    # ask user which type of interest they will be getting and ensure lowercase
    interest_type = (input("Is your interest 'simple' or 'compound'")).lower()
    if interest_type == "simple":
        # calculate and display simple interest
        simple = int(deposit * (1 + investment_interest_rate * deposit_length))
        print("You will have £" + str(simple))
    elif interest_type == "compound":
        # calculate and display compound interest
        compound = int(deposit * math.pow((1 + investment_interest_rate), deposit_length))
        print("You will have £" + str(compound))
    # return error message in user inputs incorrectly
    else:
        print("You have not entered either 'simple' or 'compound', please rerun the program and try again")

# return error message in user inputs incorrectly
else:
    print("You have not entered either 'bond' or 'investment', please rerun the program and try again")
