"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

### all your code below ###

#Setting Up varriables
n1 = 10
n2 = 20
P = 33000000000 #Elon's capital
r1 = 3.96
r2 = 4.32

#Calculation and check for 10 year
I1 = P*(1+(r1/100))**n1
print(I1)

#Calculation and check for 20 year
I2 = P*(1+(r2/100))**n2
print(I2)

# final answer for 10-year
ten_year_final = 48660509081.78675

# final answer for 20-year
twenty_year_final = 76889229275.98897

def Compounding_interest(Principal, rate, time):
    Final_Amount = Principal * (1 + (rate / 100)) ** time
    return Final_Amount

Ten_Year = Compounding_interest(P, r1, n1)
print("function used " + str(Ten_Year))

Twenty_Year = Compounding_interest(P, r2, n2)
print("function used " + str(Twenty_Year))