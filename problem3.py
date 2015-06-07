def getHighestPrime(integer):
  i = 2
  while i <= integer:
    if integer % i**2 == 0:
      integer = integer/(i**2)
    elif integer % i == 0:
      integer = integer/i
    else:
      i += 1
  return  i



print getHighestPrime(234231141)
