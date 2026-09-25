"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

JMU 2022-2023 Annual:
In-state total cost: 30792 USD
Out-of-state total cost: 47882 USD

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###
I=30792     #Setting up varriables
O=47882

P=1000000   #Converting known data into varriables
r=0.05
n=1

A = I / r   # Functions for each calculation
B = O / r

print(A)    # Checking Result
print(B)    

in_state_gift = 615840.0

out_state_gift = 957640.0
