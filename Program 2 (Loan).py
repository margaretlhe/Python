#loan.py
#This program calculates monthly mortgage payments
#written by Margaret He, ECS 10, Fall Quarter 2013

def payment():
    p = eval(input("\nWhat is the amount of the loan? "))
    apr = eval(input("What is the annual % interest rate? "))
    years = eval(input("How many years will the loan be? "))
    max = eval(input("What is the maximum amount you can afford to pay per month? "))

    n = 12*years
    apr = apr/100.00
    i = apr/12 
    m = p * i * (((1+i)**n) / (((1+i)**n)-1))

    print(p, apr, years, n, i, m)
    
    print("\nYou must make", n, "monthly payments of", m, "dollars")
    print("The total payout will be", 12*m*years, "dollars")
    print("The total interest you will pay on a loan of", p, "dollars is", (12*m*years)-p)

    if(m > max):
        print("\nUnfortunately, you cannot afford this loan.")

    else:
        print("Great, you can afford this loan.")
        
again = eval(input("How many loans would you like to calculate? "))
for i in range(again):
    print("\nLoan Calculation Number: ", i+1)
    payment()
        
print("\nThank you for using our services.")  
        
                
    
