# Just started poking around and was able to eventually get to the answer maybe one day I'll
# come back and make it into a proper function.

def getFactors(x):
  i = 1
  factors =[]
  while i <= x/i:
    if x % i == 0:
      factors.append([i, x/i])
      i += 1
    else:
      i += 1
  return factors

def getFactors3(x):
  i = 100
  factors =[]
  while i <= x/i:
    if x % i == 0 and x/i >= 100 and x/i <= 999:
      factors.append([i, x/i])
      return factors
    else:
      i += 1
  factors = factors if len(factors) > 0 else False
  return factors


def isPalinNum(number):
  digits = map(int, str(number))
  length = len(digits)
  if length % 2 == 0:
    half = length/2
    # print digits[:half], digits[:half-1:-1]
    return digits[:half] == digits[:half-1:-1]
  else:
    for place,digit in enumerate(digits):
      if digit != digits[-place-1]:
        return False
  return True


number = 999**2
i = 400
largest_palin = 906609
end = 999
while i <= end:
  isPalin = False
  while number >= largest_palin:
    if isPalinNum(number) and number % i == 0 and getFactors3(number):
      largest_palin = number
      isPalin = True
      palin_factors = getFactors3(number)
      print "Number:",i,"\n Palindrome:",number,"\n 3-digits:",palin_factors,"\n Factor:", number % i == 0, "\n Pair:", number/i
      number -= 1

    
    number -= 1

  i += 1
  number = 999**2
