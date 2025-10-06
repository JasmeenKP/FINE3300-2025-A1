# Mortgage Payment Calculator using classes for FINE3300
# Calculates mortgage payment schedules based on user inputs
# Attributes of mortgage payment: quoted rate and amortization years

class MortgagePayment:
    def __init__(self, quoted_rate, amortization_years):
        self.__quoted_rate = quoted_rate / 100  
        self.__amortization_years = amortization_years
    
    # Private method: calculating present value of annuity factor
    def __pva(self, r, n):
        return (1 - (1 + r) ** -n) / r
    
    # Public method: calculating all periodic payments
    def payments(self, principal):
        # Converting semi-annual rate to effective monthly rate
        semi_annual_rate = self.__quoted_rate / 2
        monthly_rate = (1 + semi_annual_rate) ** (1 / 6) - 1

        # Calculating number of payments for monthly schedule
        n_monthly = self.__amortization_years * 12

        # Calculating monthly payment
        monthly_payment = principal * (monthly_rate / (1 - (1 + monthly_rate) ** -n_monthly))

        # Calculating semi-monthly payment 
        semi_monthly_rate = (1 + semi_annual_rate) ** (1 / 12) - 1
        n_semi_monthly = self.__amortization_years * 24
        semi_monthly_payment = principal * (semi_monthly_rate / (1 - (1 + semi_monthly_rate) ** -n_semi_monthly))

        # Calculating biweekly payment  
        biweekly_rate = (1 + semi_annual_rate) ** (1 / 13) - 1
        n_biweekly = self.__amortization_years * 26
        biweekly_payment = principal * (biweekly_rate / (1 - (1 + biweekly_rate) ** -n_biweekly))

        # Calculating weekly payment 
        weekly_rate = (1 + semi_annual_rate) ** (1 / 26) - 1
        n_weekly = self.__amortization_years * 52
        weekly_payment = principal * (weekly_rate / (1 - (1 + weekly_rate) ** -n_weekly))

        # Calculating rapid biweekly payments
        rapid_biweekly_payment = monthly_payment / 2

        # Calculating rapid weekly payments
        rapid_weekly_payment = monthly_payment / 4

        # Returning all payments as a tuple and rounded to 2 decimal places
        return (
            round(monthly_payment, 2),
            round(semi_monthly_payment, 2),
            round(biweekly_payment, 2),
            round(weekly_payment, 2),
            round(rapid_biweekly_payment, 2),
            round(rapid_weekly_payment, 2)
        )
    
# Main program: getting user input and displaying results
if __name__ == "__main__":
    print("WELCOME TO THE MORTGAGE PAYMENT CALCULATOR! :)")
    

    # Getting User Inputs
    principal = float(input("Enter the mortgage principal amount: "))
    quoted_rate = float(input("Enter the quoted annual interest rate (ex. 2 for 2%):"))
    amortization_years = int(input("Enter the amortization period: "))

    # Creating object and calculating payments
    mortgage = MortgagePayment(quoted_rate, amortization_years)
    payments = mortgage.payments(principal)

    # Displaying results
    print("HERE ARE YOUR MORTGAGE PAYMENT OPTIONS!:")
    print("Monthly Payment: $", payments[0])
    print("Semi-monthly Payment: $", payments[1])
    print("Bi-weekly Payment: $", payments[2])
    print("Weekly Payment: $", payments[3])
    print("Rapid Bi-weekly Payment: $", payments[4])
    print("Rapid Weekly Payment: $", payments[5])