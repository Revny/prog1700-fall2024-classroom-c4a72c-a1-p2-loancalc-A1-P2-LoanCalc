#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #ask the user for there loan inputs
    loan=float(input("how much money will you borrow?"))
    interestrate=float(input("how much interest?"))
    years=float(input("how many years"))
    #times 12 months by whatever many years the user inputs
    #this was originally times 52 weeks by user inputed years but was a bit too low to feel right
    months=12*years
    #add everything together then print
    weeklypayment=(loan*interestrate*years)/months
    print(weeklypayment)





    # YOUR CODE ENDS HERE

main()