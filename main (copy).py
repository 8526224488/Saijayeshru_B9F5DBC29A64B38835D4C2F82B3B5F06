
def fact_rec lm la(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


number = int(input("Enter the value :"))
res = fact_rec(number)

print("The factorial of {} is {}.".format(number, res))
