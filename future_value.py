def calculator_future_value(p,i,t):
      return p * (( 1 + i / 100) ** t)
p = float(input("Enter present value of the account: "))
i = float(input("Enter monthly interest rate: "))
t = int(input("Enter number of months: "))
f=calculator_future_value(p,i,t)
print("Account’s future value is: ",'$' + format(f, ',.2f'))
input('Press ENTER to exit')

