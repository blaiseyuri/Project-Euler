def getPrimes(integer):
  primes = [2,3]
  for i in range(4, integer):
    length = len(primes) - 1
    n = 0
    while n <= length:
      if i % primes[n] == 0:
        break
      n += 1
    if n >= length:
      primes.append(i)
  return primes

def smallCF(integer):
  primes = getPrimes(integer)
  length = len(primes) - 1
  i = True
  while i:
    for place,prime in enumerate(primes):
      if integer % prime != 0:
        integer += 1
        break
      if place >= length:
        True
        return integer
  return [False,integer]

numbers = range(11,21)
length = len(numbers) - 1
i = True
num = 159279120
while i:
  for place,integer in enumerate(numbers):
    if place >=  7:
      print num,integer,place 
    if num % integer != 0:
      num += 1
      break
    if place >= length:
      i = False

