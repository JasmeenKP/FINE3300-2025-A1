# Exchange rate calculator reading from csv and using classes

import pandas as pd

class Exchange_Rates:
    def __init__(self):
        # Reading the CSV file (must be in the same folder as this .py file)
        self.csv_file = pd.read_csv("BankOfCanadaExchangeRates.csv")

        # Getting the last USD/CAD value using tail()
        self.usd_cad_rate = float(self.csv_file["USD/CAD"].tail(1))

    # Creating Method to convert between USD and CAD
    def convert(self, amount, from_currency, to_currency):
        # Converting USD to CAD
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.usd_cad_rate
            
        # Converting CAD to USD
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.usd_cad_rate
            
        # Same currency
        elif from_currency == to_currency:
            return amount
            
        # Only USD and CAD allowed
        else:
            print("Only USD and CAD conversions are supported.")
            return None
        

# Main program: getting user input and displaying results
# Creating Exchange_Rates object
exchange_rates = Exchange_Rates()

# Getting user input for conversion
amount = float(input("Enter the amount to convert: "))
from_currency = input("Convert from (USD or CAD, CAPS ONLY): ")
to_currency = input("Convert to (USD or CAD, CAPS ONLY): ")

# Calculating conversion
result = exchange_rates.convert(amount, from_currency, to_currency)

# Displaying result rounded to 2 decimal places
if result is not None:
    print(round(amount, 2), from_currency, "=", round(result, 2), to_currency)
